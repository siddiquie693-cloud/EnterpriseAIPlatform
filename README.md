# 🚀 Enterprise AI Knowledge Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-REST-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![LangChain](https://img.shields.io/badge/LangChain-LLM-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-purple)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-orange)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)

</p>

---

# 📖 Overview

Enterprise AI Knowledge Platform is an AI-powered backend application that enables organizations to upload, manage, search, summarize, and query enterprise documents using modern Large Language Models (LLMs).

The platform combines **Django REST Framework**, **LangChain**, **LangGraph**, **FAISS**, **Hybrid Search**, and **Retrieval-Augmented Generation (RAG)** to provide intelligent document understanding while maintaining secure user authentication and role-based authorization.

This project demonstrates production-ready backend development practices including Dockerization, cloud deployment, REST API design, vector search, AI agent orchestration, and scalable software architecture.

---

# ✨ Key Features

## 🔐 Authentication & Authorization

- JWT Authentication
- Refresh Token Support
- Secure Login & Registration
- Custom User Model
- Role-Based Access Control (RBAC)

---

## 📄 Document Management

- Upload PDF, DOCX & TXT documents
- Document Metadata Management
- Document Activation / Deactivation
- User-specific document ownership
- Secure file storage

---

## 🤖 AI Capabilities

- AI Document Summarization
- Retrieval-Augmented Generation (RAG)
- Hybrid Search
  - BM25 Keyword Search
  - FAISS Semantic Search
- Intelligent Question Answering
- Multi-Agent AI Workflow
- LLM Integration using Groq

---

## 🔍 Search Engine

- Keyword Search
- Semantic Search
- Hybrid Ranking
- Vector Embeddings
- Similar Document Retrieval

---

## 📊 Backend APIs

- RESTful API Design
- Swagger Documentation
- OpenAPI Schema
- Pagination
- Filtering
- Ordering
- Search Support

---

## 🐳 Deployment

- Docker
- Docker Compose
- PostgreSQL
- Render Cloud Deployment
- Production Settings
- Environment Variable Configuration

---

# 🏗 System Architecture

```
                    +----------------------+
                    |    Client / Frontend |
                    +----------+-----------+
                               |
                               |
                     REST API (DRF)
                               |
+--------------------------------------------------------+
|              Enterprise AI Platform                    |
|                                                        |
| Authentication Layer                                   |
| Document Management                                    |
| AI Services                                             |
| Hybrid Search Engine                                    |
| LangGraph Agent Workflow                               |
+--------------------------------------------------------+
                 |                     |
                 |                     |
          PostgreSQL            FAISS Vector DB
                 |                     |
                 +----------+----------+
                            |
                       Groq LLM API
```

---

# ⚙ Technology Stack

## Backend

- Python 3.12
- Django
- Django REST Framework

## AI

- LangChain
- LangGraph
- Groq LLM
- FAISS
- BM25

## Database

- PostgreSQL

## API Documentation

- Swagger
- drf-spectacular

## Deployment

- Docker
- Docker Compose
- Render

## Development Tools

- Git
- GitHub
- Postman

---

# 📂 Project Structure

```
EnterpriseAIPlatform/

├── accounts/
├── ai/
│   ├── agents/
│   ├── chains/
│   ├── prompts/
│   ├── services/
│   └── views/
│
├── documents/
├── users/
├── dashboard/
├── analytics/
├── common/
├── config/
├── media/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/EnterpriseAIPlatform.git

cd EnterpriseAIPlatform
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙ Environment Variables

Create a `.env` file.

```env
SECRET_KEY=

DEBUG=True

ALLOWED_HOSTS=

DB_NAME=

DB_USER=

DB_PASSWORD=

DB_HOST=

DB_PORT=

GROQ_API_KEY=

GROQ_MODEL=
```

---

# 🗄 Database

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# ▶ Run Development Server

```bash
python manage.py runserver
```

---

# 🐳 Docker

Build

```bash
docker build -t enterprise-ai-platform .
```

Run

```bash
docker-compose up --build
```

---

# 📚 API Documentation

Swagger

```
/api/docs/
```

OpenAPI Schema

```
/api/schema/
```

---

# 🔗 Live Deployment

**Application**

https://enterprise-ai-platform-vvl0.onrender.com

**Health API**

```
GET /api/health/
```

---

# 📌 Major API Endpoints

## Authentication

```
POST /api/register/

POST /api/token/

POST /api/token/refresh/
```

---

## User

```
GET /api/profile/

GET /api/users/

PUT /api/users/{id}/
```

---

## Documents

```
POST /api/documents/upload/

GET /api/documents/

GET /api/documents/{id}/

PUT /api/documents/{id}/update/

PATCH /api/documents/{id}/status/
```

---

## AI

```
POST /api/ai/summarize/

POST /api/ai/search/

POST /api/ai/ask/
```

---

# 🧪 Testing

The project APIs were tested using

- Swagger UI
- Postman

---

# 📈 Future Enhancements

- OCR Support
- Multi-language Documents
- AI Chatbot
- Email Notifications
- Redis Caching
- Celery Background Tasks
- Kubernetes Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

**Shahil Siddiquie**

Python Backend Developer | AI Engineer

GitHub

https://github.com/siddiquie693-loud

LinkedIn

https://linkedin.com/in/md-sahil-siddiquie

---

# ⭐ If you found this project useful, consider giving it a star.
