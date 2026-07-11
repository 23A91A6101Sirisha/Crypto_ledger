Markdown# Crypto Transaction Ledger (Full-Stack Asset Ledger)

A lightweight, high-performance full-stack web application designed to track, log, and calculate the absolute valuation of digital asset portfolios in real time. Built using Python, Flask, and an optimized relational database schema via SQLAlchemy.

## 🚀 Key Architectural Features
* **Stateless Data Flow:** Seamless HTTP request/response pipeline transferring structured payloads from standard client-side DOM forms into isolated backend application contexts.
* **ORM Persistence Layer:** Utilizes SQLAlchemy with an automated SQLite relational data system initialization script.
* **Defensive Input Validation:** Severe backend data processing safeguards, type-casting validations (`float`), and comprehensive `try/except` error routing middleware blocks to protect system resources.
* **Dynamic Template Interpolation:** Server-side layout calculation using Jinja2 formatting logic engines to render up-to-the-minute math valuations without additional asset network overhead.

---

## 🏗️ System Architecture & Data Pipeline

[ Frontend: Tailwind HTML ] ───(HTTP POST Payload)───> [ Backend: Flask Server ]▲                                                   ││                                           (SQLAlchemy Engine)│                                                   ▼[ Rendered Jinja2 DOM ] ◄─────(Dynamic Context)───── [ SQLite Relational DB ]
---

## 🛠️ Technology Stack
* **Backend Framework:** Python 3 (Flask Micro-framework)
* **Data Persistence Engine:** SQLite via Flask-SQLAlchemy (Object Relational Mapping)
* **Frontend Presentation:** Responsive UI layout compiled using the Tailwind CSS engine

---

## 🏁 Installation & Local Execution Guide

Follow these steps to spin up the local development gateway pipeline:

### 1. Initialize Project Directory
Clone or download the project environment and navigate directly into the terminal root execution point:
```bash
cd crypto_ledger
2. Dependencies ProvisioningInstall the baseline framework dependencies directly via your environment runtime package manager:Bashpip install flask flask-sqlalchemy
3. Launch Development Server GatewayRun the primary application context entry point. The database structures will dynamically generate automatically upon boot initialization:Bashpython app.py
4. Client AccessOpen your browser framework environment and navigate directly to the local network port address:http://127.0.0.1:5000📊 Database Schema DetailsAttributeData TypeConstraint RuleFunctional Use-CaseidIntegerPrimary Key (Autoincrement)Unique identifier reference indexing indextoken_nameString(10)Nullable=FalseCryptographic uppercase ticker symbol (e.g., BTC, ETH)amountFloatNullable=FalseHigh-precision quantity execution metricprice_usdFloatNullable=FalseGlobal fiat acquisition conversion benchmark ratetimestampDateTimeDefault=UTCLedger entry execution audit parameter
