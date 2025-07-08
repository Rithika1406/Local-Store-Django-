# 🛒 LocalStore – Django E-commerce Web App

A simple e-commerce website built with Django 5.2. Users can register, browse products, add them to a cart, checkout, and leave reviews.

---

## 📦 Features

- User registration & login (with session-based authentication)
- Product listing with filter & sort options
- Product detail page with review support
- Add to cart & cart view
- Checkout with order creation
- Admin support for managing products, orders, and users

---

## 🗂️ Project Structure

```

localstore/
│
├── localstore/           # Project settings
├── store/                # Core shopping logic: models, views, templates
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/store/
│
├── users/                # User registration & auth logic
│   ├── views.py
│   ├── urls.py
│   └── templates/users/
│
├── media/                # Uploaded media files (product images)
├── static/               # Static files (CSS, JS)
└── db.sqlite3            # SQLite database

````

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
https://github.com/Rithika1406/Local-Store-Django-

cd localstore
````

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install Django==5.2 Pillow
```

</details>

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Now visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👥 User Authentication

* Register at `/auth/register/`
* Login at `/auth/login/`
* Logout at `/auth/logout/`

---

## 🧪 Example Pages

| URL                  | Description              |
| -------------------- | ------------------------ |
| `/`                  | Product listing page     |
| `/product/<id>/`     | Product detail + reviews |
| `/add-to-cart/<id>/` | Add product to cart      |
| `/cart/`             | View cart items          |
| `/checkout/`         | Place order              |

---

## 📁 Media Files

* Product images are uploaded to `media/products/`
* Make sure `MEDIA_URL` and `MEDIA_ROOT` are properly configured in `settings.py`.

---

## 🧾 Requirements

* Python 3.9+
* Django 5.2
* Pillow (for image uploads)

---


## 🙌 Contributing

Feel free to fork and open pull requests. You can help improve features like:

* User order history
* Stripe/PayPal integration
* Product categories UI
* REST API version with Django REST Framework

