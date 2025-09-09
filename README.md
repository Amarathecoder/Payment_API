# 💳 Payment API

A **Django REST Framework**-based **Payment API** that supports **multi-currency transactions**, **real-time currency conversion**, **merchant and customer management**, **refunds**, **payouts**, **invoices**, and **dispute handling**.  
This project integrates with an external **Currency Conversion API** to ensure seamless international transactions.

---

## 🚀 Features

- 🔹 **User Authentication** — Secure token-based authentication using Django REST Framework.
- 🔹 **Merchant & Customer Management** — Create, update, and manage merchants and customers.
- 🔹 **Payment Methods** — Support for multiple payment types (cards, mobile money, bank).
- 🔹 **Transactions** — Create and track transactions with real-time currency conversion.
- 🔹 **Currency Conversion** — Fetch live exchange rates via [ExchangeRate API](https://apilayer.com/).
- 🔹 **Refunds, Payouts, Invoices & Disputes** — Full financial workflow support.
- 🔹 **Error Handling** — Graceful fallback when the exchange rate API is unavailable.
- 🔹 **RESTful Endpoints** — Clean, structured endpoints for all operations.

---

## 🛠️ Tech Stack

- **Backend:** Django 5, Django REST Framework
- **Database:** PostgreSQL (or MySQL / SQLite for local testing)
- **API Integration:** ExchangeRate API (currency conversion)
- **Authentication:** Token-based auth (DRF `authtoken`)
- **Tools:** Python 3.12, pip, virtualenv, Postman/cURL

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Payment_API.git
cd Payment_API
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a **.env** file in the root directory and add:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EXCHANGE_RATE_API_KEY=your_api_key_here
DATABASE_URL=your_database_connection_string
```

> **Note:** Sign up at [apilayer.com](https://apilayer.com/) to get your Exchange Rate API Key.

### 5️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Start the Development Server
```bash
python manage.py runserver
```

---

## 🔐 Authentication

We’re using **DRF Token Authentication**.

### 1️⃣ Obtain Token
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/   -H "Content-Type: application/json"   -d '{"username":"your_username","password":"your_password"}'
```

### 2️⃣ Use Token in Requests
Include the token in the `Authorization` header:
```http
Authorization: Token <your_token>
```

---

## 🔗 API Endpoints

| Endpoint              | Method | Description              | Auth Required |
|-----------------------|--------|--------------------------|---------------|
| `/api/merchants/`     | GET    | List all merchants       | ✅ |
| `/api/customers/`     | GET    | List all customers       | ✅ |
| `/api/payment-methods/` | GET  | List all payment methods | ✅ |
| `/api/transactions/`  | POST   | Create a new transaction | ✅ |
| `/api/refunds/`       | POST   | Create a refund          | ✅ |
| `/api/payouts/`       | POST   | Create a payout          | ✅ |
| `/api/invoices/`      | GET    | Fetch all invoices       | ✅ |
| `/api/disputes/`      | GET    | Manage disputes          | ✅ |

---

## 🌍 Currency Conversion

Transactions automatically fetch live exchange rates from the **ExchangeRate API**.  
If the API fails, we gracefully fallback to the original currency and amount.

**Example Response:**
```json
{
    "amount": "100.00",
    "currency": "USD",
    "merchant_currency": "NGN",
    "converted_amount": "153000.00",
    "exchange_rate": "1530.00"
}
```

---

## 🧪 Running Tests
```bash
python manage.py test
```

---

## 📂 Project Structure
```
Payment_API/
├── api/
│   ├── migrations/
│   ├── models.py          # Database models
│   ├── serializers.py     # Data serializers
│   ├── views.py           # API views & logic
│   ├── urls.py            # API endpoints
│   ├── tests.py           # Unit tests
├── Payment_API/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configs
├── requirements.txt
├── README.md
└── manage.py
```

---

## 📌 Next Steps

✅ **Week 1**: Project setup ✔️  
✅ **Week 2**: Authentication ✔️  
✅ **Week 3**: Currency conversion ✔️  
✅ **Week 4**: Payment logic ✔️ *(merged with Week 3)*  
🔄 **Week 5**: Write tests, documentation & prepare for presentation 🔜  

---

## 📜 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.

---

## 👩‍💻 Author

**Amarachukwu “Mimi” Ekwugha**  
📧 Email: your.email@example.com  
🌐 Portfolio: https://yourportfolio.com  
🔗 LinkedIn: https://linkedin.com/in/yourprofile
