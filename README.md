# InkredoBackend

## About

This project tries to deal with the backend requirement of the below provided requirements.

## Requirements:

- Login and access token for session management.
- Register
- User information along with the current company(with leave option) if he is working in any after login.
- User history where he has worked in the past after login.
- Opetion to create a new company.
- Company list to join if he has not joined any.
- Company page with Company list
- Each company should show present and past employee list.

## Technology used

- Django
- Postman
- sqlite3
- VScode

## Workflow

The homepage will have two cards **Employee** and **Company**, which leads to the respective dashboard. **Employee** leads to Employee DashBoard if have access tokens, other wise **login/Register** page and then the dashboard. **Employee DashBoard** will have 3 sections 1.Personal Infomation along with Current working comapny if any, 2. Employee History, 3.List of the companies to join if have not joined any.
Similarly **Company Card** will lead to the company dashboard, which shows the list of all companies, which will be clickable and show present employee list and past employee list on a new page.

## APIs

- api/token/
  - Method: Post {email, password}
- api/user/register/
  - Method: Post {email, password, full_name}
- api/user/<str:id>/company/ get/post leave/join
  - Method: Get
  - Method: Post {comapny_id}
- api/user/<str:id>/history/
  - Method: Get
- api/company/all/
  - Method: Get
- api/company/<str:id>/presentemployee/
  - Method: Get
- api/company/<str:id>/pastemployee/
  - Method: Get

## Testing

Testing of the api has been done using Postman

## How to Run

- Clone the repository.
- Create a virtual environment in the project directory and start it

```
python3 -m venv env
. env/bin/activate
```

- run the requirements.txt

```
pip install -r /path/to/requirement.txt
```

- make migrations to initialize the database and migrate.

```
python3 manage.py makemigrations
python3 manage.py makemigrations
```

- Ready to go run the server now

```
python3 manage.py runserver
```

- Still need help reach out kkarhana47@gmail.com
