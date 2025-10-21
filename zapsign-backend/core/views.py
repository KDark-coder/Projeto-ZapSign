from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .utils import extract_text_from_pdf, analyze_document_with_openai
from .models import Company, Document, Signer
from .serializers import CompanySerializer, DocumentSerializer, SignerSerializer

class AnalyzeDocumentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        pdf_url = request.data.get("pdf_url")
        if not pdf_url:
            return Response({"error": "pdf_url obrigatório"}, status=400)
        try:
            analysis = analyze_document_with_openai(pdf_url)
            return Response({"analysis": analysis})
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class SignerViewSet(viewsets.ModelViewSet):
    queryset = Signer.objects.all()
    serializer_class = SignerSerializer