# 📚 OnlineBookStore

A full-stack **online bookstore web application** built with **Python, Django, and MySQL**. Users can browse books, view details, add books to a shopping cart, update quantities, and manage cart items. This portfolio project demonstrates Django, database integration, CRUD operations, application routing, and Git/GitHub.

## 🚀 Project Overview

OnlineBookStore simulates an online bookstore and follows Django's **MVT (Model-View-Template)** architecture, using a relational database to store application data.

```text
User → Browse Books → View Details → Add to Cart → Update Quantity → Remove Item → Checkout
```

## ✨ Features

- 📚 Browse available books and view book details
- 🛒 Add books to cart, update quantities, and remove items
- 💾 Database integration and Django models
- 🔗 Django URL routing and views
- 🧩 Modular Django application structure
- 🧪 Django test structure
- 🌐 GitHub version control

## 🛠️ Technologies

| Technology | Purpose |
| --- | --- |
| Python | Backend programming |
| Django | Web application framework |
| MySQL | Database |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| Git / GitHub | Version control and code repository |

## 🏗️ Architecture

The application follows Django's MVT architecture:

```text
Frontend (HTML/CSS) → Django (Models, Views, URLs) → MySQL
```

## 📂 Project Structure

```text
OnlineBookStore/
├── manage.py
├── OnlineBookStore/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── store/
	├── migrations/
	│   └── __init__.py
	├── __init__.py
	├── admin.py
	├── apps.py
	├── models.py
	├── tests.py
	├── urls.py
	└── views.py
```

> The project structure may grow as additional features and templates are added.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/arikrishnanhp2000-beep/OnlineBookStore.git
cd OnlineBookStore
```

### 2. Create and activate a virtual environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

If the project includes a `requirements.txt` file, install its dependencies with:

```bash
pip install -r requirements.txt
```

## 🗄️ Database Configuration

Configure MySQL in `OnlineBookStore/settings.py` using your local database credentials. For example:

```python
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.mysql",
		"NAME": "onlinebookstore",
		"USER": "root",
		"PASSWORD": "your_password",
		"HOST": "localhost",
		"PORT": "3306",
	}
}
```

Create the database:

```sql
CREATE DATABASE onlinebookstore;
```

## 🔄 Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## ▶️ Run the Application

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## 🛒 Shopping Cart

Users can add books to the cart, increase or decrease quantities, and remove cart items. The checkout/order workflow can be expanded as the project develops.

## 🔗 URL Routing

Requests flow through the project URL configuration to the `store` app's URLs and views, which return a response. The app routes are in `store/urls.py`; application logic is in `store/views.py`.

## 🧠 Concepts Demonstrated

- Django projects and apps, MVT architecture, and URL routing
- Views, models, templates, and request/response handling
- Database integration, migrations, and CRUD operations
- Application-level business logic and Git/GitHub workflow

## 🧪 Testing

Run Django's test framework with:

```bash
python manage.py test
```

Tests are maintained in `store/tests.py`.

## 🔐 Security

Never commit database passwords, Django `SECRET_KEY` values, API keys, access tokens, or personal credentials. Use environment variables for sensitive configuration in production.

## 🚀 Future Enhancements

- 👤 User registration, login, and authorization
- 🔎 Book search and categories
- ❤️ Wishlist and order history
- 💳 Online payment integration
- ⭐ Book reviews and ratings
- 📧 Email notifications and admin dashboard
- 📱 Responsive UI and cloud deployment

## 🎯 Learning Outcomes

This project provided practical experience building Django applications, connecting a relational database, designing workflows, implementing CRUD and shopping-cart functionality, creating reusable apps, managing URL routing, and using Git/GitHub.

## 👨‍💻 Author

**KRISH** — Python Full Stack Developer

**Skills:** Python, Django, SQL, MySQL, HTML, CSS, Git, and GitHub.

## 🔗 Repository

[OnlineBookStore on GitHub](https://github.com/arikrishnanhp2000-beep/OnlineBookStore)

## ⭐ Project Status

| Field | Details |
| --- | --- |
| Development status | Active |
| Project type | Full-stack web application |
| Backend | Django |
| Database | MySQL |
| Version control | Git / GitHub |

## 📌 Disclaimer

This project was created for **learning, portfolio, and educational purposes** and demonstrates an online bookstore built with Python and Django.

