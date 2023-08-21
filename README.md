# Django-Authentication

This project demonstrates a basic implementation of user authentication using Django. It covers user registration, login, and logout functionality with proper security measures.

## Features

- User registration: New users can create an account with a unique username and password.
- User login: Existing users can log in using their credentials.
- User logout: Logged-in users can log out to end their session.
- Password security: User passwords are securely hashed using Django's built-in hashing mechanisms.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python [Install Python](https://www.python.org/downloads/)
- Django (install using pip): `pip install django`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ArfanAbid/Django-Authentication.git

2. Create and activate Virtual Environment:
   `python -m venv venv` then
   `.\venv\Scripts\activate`

3. Run Data base migrations:
   `python manage.py migrate`

4. Create a superuser (admin account) to access the Django admin panel:
   `python manage.py createsuperuser`

5. Run the development server:
   `python manage.py runserver`

 6. Access the development server at  `http://127.0.0.1:8000/`



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additional features.
         

