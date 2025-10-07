
# 🛒 Selenium Python Automation - Demoblaze.com

This project automates an **end-to-end shopping flow** on [Demoblaze](https://demoblaze.com/) using **Selenium with Python** and **Pytest**.  
It follows the **Page Object Model (POM)** design pattern and demonstrates real-world automation scenarios, including:

* ✅ Dynamic waits with `WebDriverWait`
* ✅ Handling modal dialogs & JavaScript alerts
* ✅ Adding products to the cart and completing checkout
* ✅ **Comprehensive test coverage** for positive and negative scenarios
* ✅ Secure credential management via environment variables (`.env`)

---

## 📂 Project Structure

```

demoblaze_test/
│── tests/                   # Test cases organized by scenario type
│   ├── negative/            # Expected failure tests (e.g., invalid login)
│   │   ├── test_login_empty_password.py
│   │   ├── test_login_empty_username.py
│   │   ├── test_login_invalid_password.py
│   │   └── test_login_invalid_username.py
│   │
│   └── positive/            # Expected success tests (e.g., successful login, checkout)
│       ├── test_login_success.py
│       ├── test_add_to_cart.py
│       └── test_checkout.py
│
│── pages/                   # Page Object Model (POM) classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
│── utils/                   # Utilities (driver setup, config, etc.)
│   ├── driver_factory.py
│   └── config.py (optional)
│
│── .env                     # Local environment variables (not committed)
│── .gitignore
│── requirements.txt
│── README.md

````

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Fay-Hosseini/selenium-demoblaze.git
cd selenium-demoblaze
````

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🔐 Setting Credentials

This project uses **environment variables** for login credentials.
Create a `.env` file in the project root (⚠️ never commit this file):

```
DEMOBLAZE_USERNAME=your_username
DEMOBLAZE_PASSWORD=your_password
```

The `.env` file is ignored via `.gitignore`.

---

## ▶️ Running Tests

Pytest automatically discovers tests in the `positive/` and `negative/` subdirectories.

**Run all tests:**

```bash
pytest -v
```

**Run only positive tests:**

```bash
pytest tests/positive -v
```

**Run only negative tests:**

```bash
pytest tests/negative -v
```

**Run a specific test file:**

```bash
pytest tests/positive/test_login_success.py -v
```

**Run tests in parallel:**

```bash
pytest -n 2
```

**Generate an HTML report:**

```bash
pytest --html=report.html --self-contained-html
```

---

## 📌 Requirements

* Python 3.8+
* Google Chrome + ChromeDriver installed
* Selenium WebDriver
* Pytest

Install all dependencies:

```bash
pip install -r requirements.txt
```

