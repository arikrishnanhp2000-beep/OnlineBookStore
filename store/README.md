# 📚 Online Book Store

A simple and user-friendly **Online Book Store web application** built using **Python, Django, MySQL, HTML, CSS, and Bootstrap**.

This project allows users to browse books, search for books, manage their shopping cart, place orders, and view their previous orders.

---

## 🚀 Features

### 👤 User Authentication

* User Registration
* User Login
* User Logout
* Authentication-based access

### 📚 Book Management

* View available books
* View book details
* Search books by title
* Display book price and stock

### 🛒 Shopping Cart

* Add books to cart
* Update book quantity
* Remove books from cart
* Calculate cart total

### 📦 Order Management

* Place orders
* Create order items
* Automatically calculate order total
* Reduce book stock after ordering
* View order success page
* View previous orders

### 🎨 User Interface

* Responsive Bootstrap design
* Professional navigation bar
* Search box
* Clean book listing

---

## 🛠️ Technologies Used

* **Python**
* **Django 6.1**
* **MySQL**
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Git & GitHub**

---

## 🗄️ Database

MySQL database used in this project:

`online_book_store`

### Main Tables

* `Book`
* `Cart`
* `Order`
* `OrderItem`
* Django `User`

---

## 📂 Project Structure

```text
OnlineBookStore/
│
├── bookstore/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── store/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```text
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project

```text
cd OnlineBookStore
```

### 3. Create Virtual Environment

```text
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```text
venv\Scripts\activate
```

### 5. Install Dependencies

```text
pip install django mysqlclient
```

### 6. Configure MySQL

Create a MySQL database:

```text
CREATE DATABASE online_book_store;
```

Update the database settings in:

```text
bookstore/settings.py
```

### 7. Run Migrations

```text
python manage.py migrate
```

### 8. Create Superuser

```text
python manage.py createsuperuser
```

### 9. Start Django Server

```text
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

Django Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

Admin can be used to add and manage books.

---

## 🔄 Application Flow

```text
Register
   ↓
Login
   ↓
Browse Books
   ↓
Search Books
   ↓
View Book Details
   ↓
Add to Cart
   ↓
Update Quantity
   ↓
Place Order
   ↓
Order Success
   ↓
My Orders
```

---

## 🧪 Testing

The following features were manually tested:

* Registration ✅
* Login ✅
* Logout ✅
* Book Listing ✅
* Search Books ✅
* Book Details ✅
* Add to Cart ✅
* Update Cart Quantity ✅
* Remove from Cart ✅
* Place Order ✅
* Order Success ✅
* My Orders ✅

---

## 🎯 Project Objective

The main objective of this project is to demonstrate practical knowledge of:

* Python programming
* Django framework
* MVC/MVT architecture
* MySQL database integration
* CRUD operations
* User authentication
* Database relationships
* Shopping cart functionality
* Order management
* Front-end development with Bootstrap

---

## 💡 Future Enhancements

Possible future improvements:

* Online payment integration
* Book categories
* Book reviews and ratings
* Wishlist
* Advanced search and filters
* Order status tracking
* User profile
* Email notifications
* Product pagination

---

## 👨‍💻 Author

**KRISH**

Python Full Stack Developer

---

## ⭐ Project Status

**Completed — Resume Ready 🚀**

```

### ⚠️ One important thing

README-ல் இந்த:

`YOUR_GITHUB_REPOSITORY_URL`

இது placeholder. **இப்போ அதை மாற்ற வேண்டாம்.** GitHub repository create பண்ணும்போது actual link போடலாம்.

மேலும் code sections-ல் இருக்கும் triple backticks **README-க்குள் தான் இருக்க வேண்டும்**. அவற்றை remove பண்ணாதீங்க.

### Next

`README.md` save பண்ணிட்டு சொல்லுங்க **“README created”**.

அதுக்கப்புறம் **GitHub repository create + upload** step-by-step போகலாம். 🚀
```
