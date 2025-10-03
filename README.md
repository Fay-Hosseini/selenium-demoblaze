# 🛒 Selenium Python Automation - Demoblaze.com

This project automates an **end-to-end shopping flow** on [Demoblaze](https://demoblaze.com/) using **Selenium with Python** and **Pytest**.
It follows the **Page Object Model (POM)** design pattern and demonstrates real-world automation challenges such as:

* ✅ Dynamic waits with `WebDriverWait`
* ✅ Handling modal dialogs & JavaScript alerts
* ✅ Adding products to cart and completing checkout
* ✅ Secure credential management via environment variables (`.env`)

---

## 📂 Project Structure

```
demoblaze_test/
│── tests/                   # Test cases
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_checkout.py
│
│── pages/                   # Page Object Model (POM) classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── product_page.py
│   └── cart_page.py
│
│── utils/                   # Utilities
│   ├── driver_factory.py
│   └── config.py (optional)
│
│── .env                     # Local environment variables (not committed)
│── .gitignore
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Fay-Hosseini/selenium-demoblaze.git
   cd demoblaze-selenium
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔐 Setting Credentials

This project uses **environment variables** for login credentials.

Create a `.env` file in the project root (⚠️ never commit this file to GitHub):

```
DEMOBLAZE_USERNAME=your_username
DEMOBLAZE_PASSWORD=your_password
```

The `.env` file is ignored via `.gitignore`.

---

## ▶️ Running Tests

Run all tests:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_login.py -v
```

Run tests in parallel:

```bash
pytest -n 2
```

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

---

## 📌 Requirements

* Python 3.8+
* Google Chrome + ChromeDriver installed
* Selenium WebDriver
* Pytest

Install all dependencies via:

```bash
pip install -r requirements.txt
```

