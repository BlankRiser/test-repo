https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc

https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

https://hackersandslackers.com/flask-sqlalchemy-database-models/

https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

https://towardsdatascience.com/deploy-a-flask-app-on-heroku-and-connect-it-to-a-jawsdb-mysql-database-10e762bc9160


## Setting up data base in heroku-postgressql

Connect our system with heroku-postgresql database
```
psql <DATABASE_URI provided by heroku-postgresql>
```
At first we can see that there's no TABLE in our database `\dt`, so we create a table from the model we made but in postgrsel format

```
CREATE TABLE github_webhook_data(
id SERIAL PRIMARY KEY,
path TEXT,
method TEXT,
headers TEXT,
body TEXT
;
```
The output would be `CREATE TABLE` if there are no issues
You can view the contents of the table using:
```
\d github_webhook_data
```