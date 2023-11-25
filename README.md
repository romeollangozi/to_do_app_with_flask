# TO-DO WEB APP

This project was for learning purposes about Flask library SQLAlchemy. I have created a simple to-do list with user authentication and a dedicated database to hold users data and to-do notes. All the website aspects where build with
Flask, SQLAlchemy was used as our ORM(Object Relational Mapper) to make queries to the database.
The database engine we used was SQLite a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, database engine. Flask-Login was used to provide user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.

## Installation

Clone this repository
```bash
git clone git@github.com:romeollangozi/to_do_list_with_flask.git
```

You should have python version 3+ installed on your machine if you haven't you can check this [tutorial](https://realpython.com/installing-python/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules to run this app

This command will install all dependences needed for this web-app to run
```bash
pip install .
```

## Usage

```bash
python3 main.py
```
or

```bash
flask --app website run
```
## License

[MIT](https://choosealicense.com/licenses/mit/)
