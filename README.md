# Little Lemon Backend Capstone

## Project Overview

This project was developed as part of the **Meta Back-End Developer Professional Certificate**. It is a backend application built using **Django** and **Django REST Framework** for the Little Lemon restaurant.

The application provides REST APIs for managing menu items, table bookings, and user authentication. It uses **MySQL** as the database and **Djoser** for token-based authentication.

---

## Technologies Used

* Python 3
* Django
* Django REST Framework
* MySQL
* Djoser
* Git & GitHub

---

## Features

* User registration
* Token-based user authentication
* Menu management API
* Table booking API
* MySQL database integration
* RESTful API implementation

---

## API Endpoints

### Home

```text
/
```

### Booking Page

```text
/booking/
```

### Menu API

```text
GET    /api/menu/
POST   /api/menu/
```

### Booking API

```text
GET    /api/bookings/
POST   /api/bookings/
```

### User Registration

```text
POST   /auth/users/
```

### User Login

```text
POST   /auth/token/login/
```

### User Logout

```text
POST   /auth/token/logout/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kusoumya2006-netizen/littlelemon.git
```

Navigate to the project directory:

```bash
cd littlelemon
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Configure the MySQL database in `settings.py`, then apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## Repository

GitHub Repository:

https://github.com/kusoumya2006-netizen/littlelemon

---

## Author

**Soumya Kumar**

Developed as part of the **Meta Back-End Developer Professional Certificate**.
