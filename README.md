# api_yatube
This project was created as a part of the Backend Python course in Yandex Practicum. 

The API allows users to create, read, update and delete posts, comments, and follow other users.

The stack used for this project includes:

- Python 3.9
- Django 3.1.7
- Django REST framework 3.12.2
- PostgreSQL 12.4

## Quick start

To start using the Yatube API project, you will need to follow these steps:

Clone the repository: You can clone the repository using the following command in your terminal:

> git clone https://github.com/AnatoliyPracticum/api_yatube.git

Set up a virtual environment: It is recommended to use a virtual environment to manage your dependencies. You can set up a virtual environment using the following command:

> python -m venv venv

Activate the virtual environment: Once you have set up the virtual environment, you can activate it using the following command:

> source venv/bin/activate

Install the dependencies: You can install the required dependencies using the following command:

> pip install -r requirements.txt

Set up the database: You will need to set up a PostgreSQL database and update the DATABASES configuration in the settings.py file with your database details.

Run the migrations: You can run the migrations to create the necessary tables in the database using the following command:

> python manage.py migrate

Run the server: You can start the development server using the following command:

> python manage.py runserver

Once you have completed these steps, you should be able to access the Yatube API at http://localhost:8000/. 
