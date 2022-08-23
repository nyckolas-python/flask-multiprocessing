## ⚙️ Run locally

1. Clone this repo and enter to the project folder SGM:
```
git clone copy/paste/link/to/repo

cd flask-multiprocessing
```

2. Install Poetry is a tool for dependency management and packaging in Python:
```
$ make install poetry
# or
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
3. Install all dependencies:
```
$ make update
# or
$ poetry update
```
4. Run the 
```
$ make start
# or
$ poetry run python app.py
```
5. Deploy on Heroku, you need have an account on heroku.com
```
$ poetry export -f requirements.txt --output requirements.txt --without-hashes
$ pip install heroku
$ heroku login
$ heroku create
$ git push heroku main
$ heroku ps:scale web=1
$ heroku open
$ heroku logs --tail
```

## ✅ Task

Terms of Reference
We need to create a web application using Flask
The first page - user authorization by login and password
Three users with three different access levels must be created in the database
After successful authorization, the user must see an empty page with the button 
"Refresh" button
After the user presses the "Refresh" button, the first ads from any OLX category will be dynamically loaded by JS using threading + requests

1. If the user's access category is 1 - the first 100 (name, price) are loaded.
2. User's access category 2 - load the first 200 (title, price, photo)
3. User access category 3 - load the first 300 (name, price, photo, seller's name)

Add the ability to sort ads by price

Elements must be saved in the database

Each item has a "delete" button, and when you click on the button, the ad will disappear from the site and from the database
