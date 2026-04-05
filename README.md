### INF601 - Advanced Programming in Python

### Nathan Birkes

### Mini Project 4

# Mini Project 4 - Quote Board

A simple Django web application that allows users to view, categorize, and submit quotes, phrases, sayings, notes, etc.

## Project Description

Quote Board is a Django web application that allows users to browse a collection of quotes, view them by category, and submit new quotes through a form. 
It includes user authentication, allowing users to register, log in, and associate quotes with their accounts. 

---

## Getting Started

### Dependencies

* Windows 10 or later
* Python 3.10+
* pip (Python package manager)
* Django

Install dependencies using:

```bash
pip install -r requirements.txt
```

### Installing

1. Download or clone the repository to your local machine:

```bash
git clone <your-repo-url>
cd quote_project
```

2. Make sure you are inside the project directory that has `manage.py`

3. Install required packages:

```bash
pip install -r requirements.txt
```

### Executing program

Follow these steps to initialize and run the project:

1. Create database migrations:

```bash
python manage.py makemigrations
```

2. Apply migrations to the database:

```bash
python manage.py migrate
```

3. Create an admin (superuser) account:

```bash
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

5. Open your browser and go to:

```
http://127.0.0.1:8000/
```

6. Access the admin panel if needed:

```
http://127.0.0.1:8000/admin/
```

## Help

Common issues:

* If templates are not loading, make sure that the `templates` folder is added in `settings.py`
* If migrations fail, delete the `db.sqlite3` file and re run the migrations
* Make sure the `quotes` app is added to the `INSTALLED_APPS`

Run the server again if issues still happen:

```bash
python manage.py runserver
```

## Authors

Nathan Birkes

## Version History

* 0.1
  * Initial Release

## License

This project is for educational use and does not currently include a specific license.

## Acknowledgments

Inspiration, code snippets, and resources:

* https://docs.djangoproject.com/
* https://github.com/nsbirkes/miniproject3NathanBirkes