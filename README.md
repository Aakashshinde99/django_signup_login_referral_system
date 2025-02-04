# 🎯 Django Referral System

A simple Django-based referral system that allows users to sign up, log in, and refer new users using a unique referral code. Built using Django and SQLite, this project demonstrates fundamental user authentication and referral tracking.

---

## 🚀 Features

- ✅ **User Registration** with referral tracking
- ✅ **User Login** and authentication
- ✅ **Unique Referral Code Generation**
- ✅ **Referee Tracking** (View who signed up using a referral code)
- ✅ **Admin Panel Access** for user management
- ✅ **Database Management** with SQLite
- ✅ **Deployable on AWS**

---

## 🛠️ Tech Stack

| Technology  | Description |
|-------------|------------|
| Django      | Python web framework for rapid development |
| SQLite      | Lightweight database for local development |
| HTML, CSS   | Frontend templates for signup, login & home |
| AWS        | Deployment on AWS EC2 with Nginx & Gunicorn |

---

## 📂 Project Structure

```
referral_login_project/
│── referral_system/
│   ├── users/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── users/
│   │   │   │   ├── signup.html
│   │   │   │   ├── login.html
│   │   │   │   ├── home.html
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── urls.py
│   ├── settings.py
│   ├── urls.py
│── manage.py
│── requirements.txt
│── README.md
```

---

## 📥 Installation & Setup

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/django-referral-system.git
cd django-referral-system
```

### 🔹 Step 2: Create and Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### 🔹 Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 🔹 Step 5: Create Superuser (For Admin Panel)
```bash
python manage.py createsuperuser
```

### 🔹 Step 6: Run the Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** to access the application.
