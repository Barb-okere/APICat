# APICat
E-commerce API - Django Project
This project defines a simple e-commerce API using Django REST Framework (DRF) to manage Customers, Orders, and Order Items.

Setting Up the Environment and Running the API
Install Python and Dependencies:
Ensure you have Python (version 3.6 or later) and pip (package manager) installed on your system. You can download them from https://www.python.org/downloads/.
Create Virtual Environment (Optional):
It's recommended to create a virtual environment to isolate project dependencies. Use venv or virtualenv depending on your Python version:
Bash
python -m venv venv  # Using venv
Use code with caution.

Activate the virtual environment:
Bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate.bat  # Windows
Use code with caution.

Install Dependencies:
Install Django and Django REST Framework inside the virtual environment:
Bash
pip install django djangorestframework
Use code with caution.

Project Structure
ecommerce_api/
├── manage.py
├── ecommerce_api/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── models/  # Your models.py file goes here
└── tests/  # Testing script will be placed here (optional)
Note: This assumes you have a models.py file with your models defined. Replace the placeholder with your actual file.

Create Django Project:
Navigate to your desired project directory and run:
Bash
django-admin startproject ecommerce_api
Use code with caution.

Copy Models (if applicable):
If you have a separate models.py file, copy it to the models directory within your project.
Running the Development Server
Configure Settings:
Edit ecommerce_api/settings.py and configure database settings, installed apps (include 'rest_framework'), and any other necessary options.
Migrate Database:
Run database migrations to create tables based on your models:
Bash
python manage.py makemigrations
python manage.py migrate
Use code with caution.

Start Server:
Start the Django development server:
Bash
python manage.py runserver
Use code with caution.

Access the browsable API at http://127.0.0.1:8000/api/ to explore available endpoints.
Testing the API (Optional)
Testing Script (Create a tests.py file in your project):

You can write Python scripts to test API endpoints with requests library. Here's an example:
<!-- end list -->

Python
import requests

# Replace with your actual API base URL
base_url = "http://127.0.0.1:8000/api/"

# Example: Create a customer
customer_data = {"name": "John Doe", "email": "john.doe@example.com", "phone_number": "+1234567890", "address": "123 Main St"}
response = requests.post(f"{base_url}customers/", json=customer_data)
print(f"Create Customer Response: {response.status_code}, {response.json()}")

# Example: Get all customers
response = requests.get(f"{base_url}customers/")
print(f"Get All Customers Response: {response.status_code}, {response.json()}")

# ... Add tests for other endpoints and functionalities ...
Use code with caution.

Run Tests:

Execute your testing script from the command line:
Bash
python tests.py
Use code with caution.

Uploading Project to GitHub
Create a GitHub Repository:
Create a new repository on your GitHub account.
Initialize Git:
Open a terminal in your project directory and initialize a Git repository:
Bash
git init
Use code with caution.

Add Files:
Add all files to the staging area for version control:
Bash
git add .
Use code with caution.

Commit Changes:
Commit the changes with a descriptive message:
Bash
git commit -m "Added E-commerce API with models and tests"
Use code with caution.

**Link
