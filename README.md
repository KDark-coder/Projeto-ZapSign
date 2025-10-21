# Desafio Técnico - ZapSign

## Introdução

Este projeto foi desenvolvido para o desafio técnico da ZapSign.  
Aqui estão as principais funcionalidades implementadas, as dificuldades encontradas e pontos de melhoria — tudo descrito de forma honesta e transparente.

---

## O que foi entregue

### Backend (Django + DRF + PostgreSQL)

- **Modelos criados:**  
  - Company (inclui campo `api_token` para integração com ZapSign)
  - Document (com campos para integração: `open_id`, `token`, etc.)
  - Signer (relacionado a Document)

- **Integração com ZapSign:**  
  - Ao criar um documento, o backend envia os dados para a API da ZapSign, recebe o token e o open_id, e armazena esses dados no banco.

- **Integração com IA:**  
  - O backend tem um endpoint que faz análise do conteúdo do documento usando IA (ex: OpenAI/HuggingFace) e retorna tópicos faltantes, resumo e insights.

- **Endpoints RESTful:**  
  - CRUD para Document implementado.
  - Company e Signer estão parcialmente implementados (modelos e parte do CRUD).

- **Autenticação:**  
  - Endpoints protegidos por token.

- **Testes automatizados:**  
  - Exemplos de testes Pytest para rotas principais.

- **Setup e estrutura:**  
  - Banco de dados PostgreSQL configurado.
  - Migrations prontas.
  - Instruções no README para rodar e testar o backend.

---

### Frontend (Angular)

**Não consegui finalizar o frontend.**

#### O que foi tentado:
- Criação de componentes standalone para Document (lista, formulário).
- Implementação de serviços Angular para consumir a API do backend.
- Tentativas de rodar como SPA (`ng serve`) e SSR (`ng run zapsign-frontend:serve-ssr`), mas não funcionou devido a erros NG0401 e problemas de configuração.

#### Dificuldades principais:
- Erros recorrentes na configuração do Angular Standalone e SSR.
- Incompatibilidade de scripts e rotas.
- Investi bastante tempo tentando resolver, mas não consegui superar os problemas técnicos a tempo de entregar um frontend funcional.

#### O que ficou faltando:
- Aplicação Angular funcional rodando (SPA ou SSR).
- CRUD visual fluido, mensagens de sucesso/erro.
- Testes Jest no frontend.
- Painel visual de CRUD e integração com IA.

---

## Instruções para rodar o backend

1. **Clone o projeto**
2. **Configure o banco PostgreSQL**
   - Ajuste as credenciais no `.env` ou `settings.py`.
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
4. **Rode as migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```
6. **Importante:**  
   Acesse o painel de administração Django pelo endereço  
   `http://localhost:8000/admin/`  
   O acesso por `http://127.0.0.1:8000/admin/` pode não funcionar corretamente, dependendo do ambiente ou navegador.

7. **Testar endpoints**
   - Use o DRF browsable API, Postman ou curl.

8. **Testes automatizados**
   ```bash
   pytest
   ```

---

## Integrações realizadas

- **ZapSign API:**  
  - Criação de conta no sandbox, coleta de token, integração via endpoint REST (funciona no backend).
- **IA para análise de documentos:**  
  - Endpoint para análise automática de documentos usando IA (funciona no backend).

---

## O que ficou faltando

- **Frontend Angular funcional:**  
  - Não consegui entregar a interface fluida solicitada devido a problemas técnicos e limitações de tempo.
- **CRUD completo para Company e Signer:**  
  - Implementação parcial.
- **Workflow n8n demonstrativo:**  
  - Endpoints RESTful preparados, mas não montei o fluxo/exemplo.
- **Dockerfile/docker-compose:**  
  - Setup local planejado, mas não incluído explicitamente.
- **Documentação detalhada de todos endpoints:**  
  - Exemplos básicos disponíveis, mas sem documentação formal extensa.

---

## Dificuldades técnicas enfrentadas

- **Angular SSR Standalone:**  
  - Erros NG0401, scripts ausentes, incompatibilidade de configuração no Angular 17+.
- **Build e scripts:**  
  - Falha ao rodar scripts recomendados, problemas com package.json, incompatibilidade entre SPA, SSR e estrutura do projeto.
- **Estrutura de arquivos Angular:**  
  - Dificuldade em ajustar componentes, imports, rotas e bootstrap para rodar localmente.
- **Cansaço e limitação de tempo:**  
  - Investi várias horas tentando corrigir os problemas do frontend, o que impactou a entrega.

---

## Pontos fortes da entrega

- Backend funcional, testável e integrado com ZapSign e IA.
- Endpoints RESTful e autenticação implementados.
- Testes automatizados no backend.
- Instruções claras para rodar e testar o sistema.
- Estrutura pronta para evolução futura.

---

## Pontos de melhoria e próximos passos

- Refatorar/configurar o frontend Angular para rodar como SPA (sem SSR, se necessário).
- Finalizar CRUD visual para Company e Signer.
- Criar workflow n8n demonstrativo.
- Adicionar Dockerfile/docker-compose para facilitar setup local.
- Expandir testes automatizados e documentação.

---

## Observações finais

Apesar das dificuldades técnicas, principalmente no frontend Angular, acredito que a entrega cobre as partes mais críticas do backend e integrações.  
Fui transparente sobre os problemas encontrados e o que ficou pendente.  
Agradeço pela oportunidade, estou disponível para explicar decisões, debugar ao vivo e seguir evoluindo o projeto.

---

**Contato para dúvidas ou revisão:**  
- [nsdbferreira@gmail.com]  
- Desde já, agradeço imensamente a oportunidade!
