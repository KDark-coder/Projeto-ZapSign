import pytest
from core.models import Company
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
def test_document_ai_analysis(monkeypatch):
    # Mock da função de análise IA para evitar chamada real ao OpenAI
    def mock_analyze_document_with_openai(pdf_url):
        return {
            "summary": "Resumo gerado pela IA",
            "insights": "Insights gerados",
            "missing_topics": "Tópicos faltantes"
        }
    import core.utils
    monkeypatch.setattr(core.utils, "analyze_document_with_openai", mock_analyze_document_with_openai)

    User = get_user_model()
    user = User.objects.create_user(username='testuser', password='senha123')
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    company = Company.objects.create(
        name="Empresa Teste",
        api_token="f7b22d0b-e002-472a-9d3a-27121bee79edff90176e-7dcf-443c-b1d5-b36f9837e49f"
    )

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    url = reverse("document-list")
    payload = {
        "company": f"http://localhost:8000/api/companies/{company.id}/",
        "name": "Contrato AI Teste",
        "pdf_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "signer_name": "Fulano Teste",
        "signer_email": "fulano@email.com"
    }
    response = client.post(url, payload, format="json")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Contrato AI Teste"
    assert data["status"] == "pending"
    assert "token" in data
    assert "company" in data
    assert "created_at" in data