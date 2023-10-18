# Django Workshop

## Packages installed:

- django
- bcrypt


## Useful tools
- Github Copilot for code generation
- SQLite extension in VSCode for analysing the content of SQLite databases


## TODO
- Create a login endpoint.
- Create endpoints for getting the products and adding more products.
- Use a login_required decorator for verifying login information before handling a request.

## Main Commands
```sh
# creating a virtual environment
python -m venv env

# activating an environment
# Windows
.\env\Scripts\activate

# Linux / Mac
./env/bin/activate


# for installing a package
pip3 install package

# for creating the workspace 
django-admin createproject workshop

# for creating the api for the endpoing
cd workshop # (the working directory must be the project folder)
python manage.py createapp api

# for adding the data models created to the migration
python manage.py makemigrations

# for migrating a database
python manage.py migrate

# for creating a superuser for admin tasks
python manage.py createsuperuser

# for running the server
python manage.py runserver

```

## Possible issues

- CSRF token -> in Postman, make a GET request to the /admin endpoint of the site; and get the CSRF token from the response headers. Then, in each request, use the token -> in the request headers, add the key X-CSRFToken and the value in the token

