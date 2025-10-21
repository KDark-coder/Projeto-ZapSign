from rest_framework import serializers
from .models import Company, Document, Signer
import requests
import base64

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'id', 'name', 'api_token', 'created_at']

class SignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signer
        fields = ['url', 'id', 'document', 'name', 'email', 'status', 'created_at']

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    signer_name = serializers.CharField(write_only=True)
    signer_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Document
        fields = ['url', 'id', 'company', 'name', 'pdf_url', 'open_id', 'token', 'status', 'created_at', 'signer_name', 'signer_email']

    def create(self, validated_data):
        signer_name = validated_data.pop('signer_name')
        signer_email = validated_data.pop('signer_email')
        company = validated_data['company']

        # Se company for inteiro, busque o objeto Company
        if isinstance(company, int):
            company = Company.objects.get(id=company)
        print("TOKEN QUE ESTÁ INDO PARA ZAPSIGN:", company.api_token)

        # Baixando o PDF da URL e convertendo para base64
        pdf_url = validated_data.get("pdf_url") or ""
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code != 200:
            raise serializers.ValidationError("Não foi possível baixar o PDF da URL fornecida.")

        base64_pdf = base64.b64encode(pdf_response.content).decode("utf-8")

        api_url = "https://sandbox.api.zapsign.com.br/api/v1/docs/"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {company.api_token}"
        }

        # Agora montando o payload correto para a ZapSign
        data = {
            "name": validated_data.get("name") or "",
            "base64_pdf": base64_pdf,
            "signers": [{
                "name": signer_name or "",
                "email": signer_email or ""
            }]
        }

        print("Requisição enviada:", data)
        print("Headers:", headers)

        response = requests.post(api_url, json=data, headers=headers)
        print("Status:", response.status_code)
        print("Resposta ZapSign:", response.text)

        response.raise_for_status()
        zapsign_data = response.json()

        # Salvar no banco os dados retornados
        validated_data["open_id"] = zapsign_data.get("open_id")
        validated_data["token"] = zapsign_data.get("token")
        validated_data["status"] = zapsign_data.get("status")

        # Remover o campo company do validated_data para evitar duplicidade
        validated_data.pop("company", None)
        document = Document.objects.create(company=company, **validated_data)

        Signer.objects.create(
            document=document,
            name=signer_name,
            email=signer_email,
            status=zapsign_data.get("status")
        )
        return document