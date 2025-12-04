# Installation

- create a venv
- activate venv
- install dependencies `pip install -r requirements.txt`
- run db migrations `python manage.py migrate`
- add license key to `newrelic.ini`
- create admin account `python manage.py createsuperuser`
- run the app `python manage.py runserver`
- go to admin (`http://127.0.0.1:8000/admin/`), "Pages" -> "Home"
- click the plus icon to add one child page of each type (generic and auto-detected) and make a note of the "slug" (under the "Promote" tab).
- visit the three pages in your browser
  - home `http://127.0.0.1:8000/`
  - generic `http://127.0.0.1:8000/<generic-page-slug>`
  - auto-detected `http://127.0.0.1:8000/<auto-detected-page-slug>` and `http://127.0.0.1:8000/<auto-detected-page-slug>/routable`
