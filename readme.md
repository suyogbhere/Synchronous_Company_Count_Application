# Project Name  (Company Count Application)

https://github.com/suyogbhere/Company_Count_Application/tree/master

- Python Version: Python 3.12.0
- Bootstrap Version: 4.0
- Database version: Postgresql 17


## Features

- Feature 1: User can Signup, Login, logout
- Feature 2: User can upload csv file into project
- Feature 3: User can filter the data and show of those data count on front end
- Feature 4: Django all auth authentication are used in project
- Feature 5: Only authenticated user can view inside project feature.

## Demo


## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/suyogbhere/Company_Count_Application/tree/master
    cd https://github.com/suyogbhere/Company_Count_Application/tree/master
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. cd company_count_application

5. Apply migrations (if applicable):
    ```bash
    python manage.py migrations
    python manage.py migrate
    ```
6. If you want your own superuser account run below commmand
    python manage.py createsuperuser

7. Start the development server:
    ```bash
    python manage.py runserver


## Usage

- Access the portal at http://127.0.0.1:8000
- Log in using default admin credentials (set in the admin panel).
- Upload company data csv and view thier count in the dashboard.


## project Urls

1. http://127.0.0.1:8000/accounts/login/
2. http://127.0.0.1:8000/accounts/signup/

## API Urls
1. http://127.0.0.1:8000/api/companydata/
2. http://127.0.0.1:8000/api/fileupload/