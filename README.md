# 🧪 REST API Automation Framework

This project is a Python-based API automation framework built using pytest for testing REST APIs. It supports CRUD operations validation, schema validation, and modular scalable test design.

---

## 📁 Project Structure

rest-api-automation/
│
├── config/              # Configuration files (base URLs, env configs)
├── data/                # Test data (payloads, input JSON/YAML)
├── helpers/             # Utility functions (request handlers, loaders)
├── reports/             # Test execution reports
├── schemas/             # JSON schema validation files
├── tests/               # Test cases (CRUD API tests)
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies

---

## 🚀 Features

- Create Task API testing
- Get Task by ID validation
- Update Task verification
- List Tasks validation
- Schema validation using JSONSchema
- Reusable request utilities
- Modular and scalable framework design

---

## 📦 Installation

### Clone repository
git clone <repo-url>
cd rest-api-automation

### Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

---

## 📄 Requirements

pytest  
requests  
jsonschema  
PyYAML  

---

## ⚙️ Pytest Configuration (pytest.ini)

[pytest]
addopts = -v -s
testpaths = tests
python_files = test_*.py
python_functions = test_*

---

## ▶️ Running Tests

Run all tests:
pytest

Run with verbose output:
pytest -v -s

Run specific test file:
pytest tests/test_CRUD_Operations.py

---

## 🧪 Test Flow

Create Task → Get Task → Update Task → List Tasks → Schema Validation

---

## 📌 Sample API Payload

{
  "content": "Api_Automation",
  "user_id": "test_user",
  "is_done": false
}

---

## 📊 Reports

All reports are generated under:
reports/

---

## 🧠 Key Highlights

- Modular framework design
- Externalized test data
- Schema validation using JSONSchema
- Reusable API helpers
- Ready for CI/CD integration

---

## 👨‍💻 Author

Nagesh Allur  
QA Automation Engineer | API Testing | Pytest Framework Design

---

## 🚀 Future Enhancements

- GitHub Actions CI/CD pipeline
- Allure reporting dashboard
- Docker support
- Parallel execution with pytest-xdist
- Logging framework integration
