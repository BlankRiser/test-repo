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


## Setting up our database using heroku-postgressql

1. Create an app on heroku and in `Resources` tab and search for `Heroku Postgres` and add it to our app
2. Now, click on `Heroku Postgres`, go to `Settings` tab and view credentials, Copy the **URI**
3. Connect our system with heroku-postgresql database and creating a table `github_webhook_data` that's similar to [models.py](models.py)
```
psql <DATABASE_URI provided by heroku-postgresql>
```
4. At first we can see that there's no TABLE in our database using `\dt`, so we create a table similar to [models.py](models.py)
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
5. You can view the contents of the table using:
```
\d github_webhook_data
```
You can also view the data in the TABLE github_webhook_data by creating a dataclip in `Heroku Postgres` in our Heroku app
```sql
SELECT * FROM TABLE github_webhook_data
```

6. The last step would be to include the URI in [app.py](app.py), You can do so by adding a configuration to flask

```python
app.config['SQLALCHEMY_DATABASE_URI']=''
```
