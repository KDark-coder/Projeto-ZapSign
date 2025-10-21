from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Document(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    pdf_url = models.URLField()
    open_id = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Signer(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="signers")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)