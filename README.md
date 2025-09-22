# 🚀 Описание проекта  
Тестовое задание для компании IT_One

## 🛠 Технологии
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-00A98F?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-920000?style=for-the-badge&logo=pydantic&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6A00?style=for-the-badge&logo=allure&logoColor=white)


## 🧪 Переменные окружения
Проект использует переменные окружения из файла `.env`. Создайте его на основе примера:
   ```bash
    cp .env.example .env
   ```
Затем отредактируйте `.env` файл, указав свои значения:
```ini
# .env.example
SELENIUM.BASE_URL="http://localhost:8080"
SELENIUM.HEADLESS=False
SELENIUM.TIMEOUT=10

HTTPX.BASE_URL="http://localhost:8080/external"
HTTPX.TIMEOUT=100

KAFKA.BOOTSTRAP_SERVERS=["localhost:9092"]

USER.LOGIN="user@mail.com"
USER.PASSWORD="user"

ADMIN.LOGIN="admin@mail.com"
ADMIN.PASSWORD="admin"
```

## ⚙️ Установка
1. Клонировать репозиторий:  
   ```bash
   git clone https://github.com/zomlik/techno-store-tests.git
   ```
2. Создать виртуальное окружение:  
   Linux/MacOs
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```  
   Windows
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Запуск тестов:
    ```bash
   pytest --alluredir allure-report
   ```
   
5. Allure-Reports
```bash
    allure serve allure-report
```
