import openai
import requests
import io
from PyPDF2 import PdfReader
from django.conf import settings

def extract_text_from_pdf(pdf_url):
    response = requests.get(pdf_url)
    response.raise_for_status()
    pdf_file = io.BytesIO(response.content)
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

def analyze_document_with_openai(pdf_url):
    text = extract_text_from_pdf(pdf_url)
    prompt = f"Analise o conteúdo abaixo e retorne: 1) Resumo, 2) Tópicos faltantes, 3) Insights úteis.\n\n{text}"
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512
    )
    result = response.choices[0].message.content
    # Aqui você pode tratar para separar resumo, tópicos, insights (ex: split, regex, etc)
    # Para exemplo, vamos retornar tudo como summary
    return {
        "summary": result,
        "insights": "",
        "missing_topics": ""
    }