# OWASP Top Ten Vulnerabilities Demonstration Project

## Description

This Django project has been designed to demonstrate common security vulnerabilities listed by the OWASP Top Ten. The project includes examples of vulnerabilities such as SQL Injection, XSS, Sensitive Data Exposure, Insecure Deserialization, and more.

## Technologies Used

- Python 3.x
- Django 5.x
- lxml (for XML processing)
- jsonpickle (for secure serialization and deserialization)

## Installation

### Prerequisites

Make sure you have Python and pip installed on your machine. Clone the repository and install the dependencies:

```bash
git clone https://github.com/mathisdesaulty/OWASPFixIt.git
cd OWASPFixIt/owasptopten
pip install -r requirements.txt
python manage.py makemigration
python manage.py migrate
```

You also have to create a super user:
```bash
python manage.py createsuperuser
```
He is going to be usefull for one flaw.


### Run the Server
Start the Django development server:
```bash
python manage.py runserver
```
Access the application in your browser at: http://127.0.0.1:8000/

## Features
### Demonstration of Vulnerabilities:

- SQL Injection: Examples of vulnerable SQL queries.
- XSS: Demonstration of Cross-Site Scripting vulnerability.
- Sensitive Data Exposure: Scenarios where sensitive data may be exposed.
- Insecure Deserialization: Examples using pickle and how to mitigate attacks.
- XXE: Demonstration of XML External Entity attacks and how to prevent them.

