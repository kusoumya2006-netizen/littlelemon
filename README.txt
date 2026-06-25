# Little Lemon Backend Capstone

## Project Overview

This project is the backend API for the Little Lemon Restaurant developed using Django and Django REST Framework. It provides RESTful endpoints for menu management, table bookings, and user authentication.

## Technologies Used

* Python
* Django
* Django REST Framework
* Djoser
* MySQL
* Token Authentication
* Git & GitHub

## Features

* User registration and authentication
* Menu API
* Table booking API
* MySQL database integration
* RESTful API implementation

## API Endpoints

### Home Page

```
/
```

### Booking Page

```
/booking/
```

### Menu API

```
GET  /api/menu/
POST /api/menu/
```

### Booking API

```
GET  /api/bookings/
POST /api/bookings/
```

### User Registration

```
POST /auth/users/
```

### User Login

```
POST /auth/token/login/
```

### User Logout

```
POST /auth/token/logout/
```

## Authentication

This project uses Token Authentication provided by Djoser and Django REST Framework.

## Running the Project

1. Install dependencies

```
pip install -r requirements.txt
```

2. Configure the MySQL database in `settings.py`.

3. Apply migrations

```
python manage.py migrate
```

4. Start the development server

```
python manage.py runserver
```

5. Open the application at:

```
http://127.0.0.1:8000/
```

## Repository

GitHub Repository:
https://github.com/kusoumya2006-netizen/littlelemon

---

Developed as part of the Meta Back-End Developer Professional Certificate Capstone Project.
