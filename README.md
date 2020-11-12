# GitHub Webhook using Flask
(In Development)



# References

[Webhooks](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)

[Connecting Flask with PostgresSQL](https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc)

## Setup

-  Install all the dependencies after activating your python environment
```
source venv/bin/activate
pip install flask
```

- Run app.py
```
python app.py
```
- The output from ngork would be running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/ )
- Run ngork on port 5000
    -- You can download ngrok, extract it and add it in your $PATH before executing the script below
    ```
    sudo cp ngrok /usr/local/bin
    ```
```
ngork http 5000
```
- Adding webhook to Github
    - Go to `settings` -> `Webhooks` -> Click `Add webhook`
    - Paste the ngork url as the <strong>Payoad URL</strong> and choose `application/json` as content type. 
    - Let the trigger be `send me everything`
    - Add webhook
- Doing any activity in Github would generate a `data.json`


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
You can also view the data in the TABLE github_webhook_data by creating a dataclip
```sql
SELECT * FROM TABLE github_webhook_data
```


## Setting up oauth with Github

https://github.com/settings/applications/new