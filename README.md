# 📈 Distributed Stock Market Watchlist & Analytics API

Production‑grade backend system built with **Django + Django REST Framework** for managing stock watchlists, real‑time pricing, historical analytics, and alerts.
This project was developed as a **take‑home assignment for Navya Advisors** and focuses on **scalability, clean architecture, async processing, and security**.

---

## 🚀 Features

### Core

* Custom user model with account tiers (Admin / Premium / Standard)
* JWT authentication (access + refresh tokens)
* Role‑based access control (RBAC)
* Stock master data management (Admin only)
* Watchlists with multiple stocks per user
* Historical stock price storage (time‑series)
* Async price ingestion using Celery
* Redis caching (ready for latest price caching)
* PostgreSQL as primary database
* Dockerized setup (one‑command startup)

### Advanced (Extensible)

* Background jobs for price ingestion
* Alert evaluation architecture (price thresholds)
* Optimized queries (no N+1 issues)
* Cursor‑based pagination
* Clean domain‑driven app separation

---

## 🧱 Architecture Overview

The system follows **Domain‑Driven Design** and **12‑Factor App principles**.

```
apps/
├── accounts        # Auth, users, RBAC
├── stocks          # Stock master data
├── pricing         # Stock price history & analytics
├── watchlists      # User watchlists
├── notifications   # Alerts & notifications (extensible)
config/             # Project configuration
```

### Key Design Decisions

* **Separated stock master data from price time‑series** for performance
* **Async tasks (Celery)** for external API calls and alert processing
* **Redis** used for caching, background jobs, and rate‑limiting potential
* **JWT auth** for stateless, scalable authentication

---

## 🛠️ Tech Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | Django 4 + DRF          |
| Auth             | JWT (SimpleJWT)         |
| Database         | PostgreSQL              |
| Cache / Broker   | Redis                   |
| Async Jobs       | Celery                  |
| Containerization | Docker & Docker Compose |

---

## 📦 Installation & Setup

### Prerequisites

* Python 3.11+
* Docker & Docker Compose

---

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd StockWatch
```

---

### 2️⃣ Environment Variables

Create a `.env` file:

```env
DEBUG=1
SECRET_KEY=supersecret
DB_NAME=stockwatch
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
REDIS_URL=redis://redis:6379/0
```

---

### 3️⃣ Build & Run with Docker

```bash
docker compose up --build
```

Apply migrations:

```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Application will be available at:

```
http://localhost:8000
```

---

## 🔐 Authentication

JWT‑based authentication using **SimpleJWT**.

### Login

```
POST /api/v1/auth/login/
```

Response:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

---

## 📡 API Endpoints (v1)

### Auth

* `POST /api/v1/auth/login/`

### Stocks (Admin only)

* `GET /api/v1/stocks/`
* `POST /api/v1/stocks/`

### Pricing

* `GET /api/v1/prices/latest/<symbol>/`

### Watchlists

* `GET /api/v1/watchlists/`
* `POST /api/v1/watchlists/`
* `DELETE /api/v1/watchlists/{id}/`

All responses follow a consistent RESTful structure.

---

## ⚙️ Background Jobs

Celery workers handle:

* Periodic stock price ingestion
* (Extensible) alert evaluation

Start worker (Docker already configured):

```bash
celery -A config worker -l info
```

---

## 🧪 Testing Strategy (Planned)

* Unit tests for:

  * Models
  * Managers
  * Serializers
* Integration tests for:

  * Auth flows
  * Watchlist workflows
* Background task testing

Target: **80%+ coverage for core modules**

---

## 🔍 Performance Optimizations

* Indexed stock symbols & timestamps
* `select_related` / `prefetch_related`
* Cursor‑based pagination
* Async processing for expensive operations
* Redis‑ready caching layer

---

## 🔒 Security Considerations

* JWT token rotation
* Stateless authentication
* RBAC enforcement
* Soft‑delete users (no hard deletes)
* Admin‑only stock master updates

---

## 📈 Scalability Considerations

* Horizontal scaling via stateless API
* Background workers scale independently
* Redis used as shared cache and broker
* PostgreSQL optimized for time‑series queries

---

## 📌 Trade‑offs & Assumptions

* External stock API mocked for simplicity
* Email notifications mocked
* Alerts framework designed but not fully wired

---

## 👨‍💻 Author

 Ayush Neupane

---

## ✅ Conclusion

This project demonstrates:

* Clean backend architecture
* Scalable async workflows
* Secure authentication & authorization
* Production‑ready Django API practices

Designed to be **extendable, testable, and cloud‑ready**.
