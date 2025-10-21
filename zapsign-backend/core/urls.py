from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, DocumentViewSet, SignerViewSet, AnalyzeDocumentView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'signers', SignerViewSet)

urlpatterns = [
    path('analyze/', AnalyzeDocumentView.as_view(), name='analyze-document'),
    path('', include(router.urls)),  # <-- Inclui as rotas do router!
    # ... outros endpoints ...
]