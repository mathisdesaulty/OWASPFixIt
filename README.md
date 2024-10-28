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
git clone https://github.com/yourusername/your-repo.git
cd your-repo
pip install -r requirements.txt
```
Run the Server
Start the Django development server:

bash
Copier le code
python manage.py runserver
Access the application in your browser at: http://127.0.0.1:8000/

Features
Demonstration of Vulnerabilities:

SQL Injection: Examples of vulnerable SQL queries.
XSS: Demonstration of Cross-Site Scripting vulnerability.
Sensitive Data Exposure: Scenarios where sensitive data may be exposed.
Insecure Deserialization: Examples using pickle and how to mitigate attacks.
Fixed Version:

Utilizing jsonpickle for secure serialization/deserialization to avoid issues related to pickle.
Testing
Insecure Deserialization
Navigate to the insecure deserialization page.
Upload a malicious pickle file to see how the server handles it.
Secure Deserialization
Navigate to the secure deserialization page.
Upload a valid JSON file serialized with jsonpickle.
### Additional Notes

- Make sure to replace the placeholder `yourusername` and `your-repo` in the GitHub clone command with your actual GitHub username and repository name.
- You can also add more sections or modify existing ones based on your project's specifics or additional features you want to highlight. 

Feel free to reach out if you need any further modifications or additional information!
