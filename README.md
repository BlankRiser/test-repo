# GitHub Webhook using Flask
(In Development)

This repo is for testing purposes only <br />
The main repo is [github-webhook-store](https://github.com/fifthtry/github-webhook-store)

## Setup

1. Install all the dependencies after activating your python environment
```
source venv/bin/activate
pip install flask Flask==1.1.2 Flask_SQLAlchemy==2.4.4 gunicorn==19.9.0 psycopg2
```

2. Run app.py
```
python3 app.py
```

3. Run [ngork](https://ngrok.com/download) on the port flask opens development server, for me it is [ttp://127.0.0.1:5000/](http://127.0.0.1:5000/ ), so port 5000
    - You can download ngrok, extract it and add it to your `$PATH` before executing ngrok on your development server.
    ```
    sudo cp ngrok /usr/local/bin
    ngork http 5000
    ```
4. Adding webhook to a Github repository
    - Go to **settings** -> **Webhooks** -> Click **Add webhook**
    - Paste the ngork url as the ***Payoad URL*** and choose `application/json` as content type. 
    - Let the trigger be `send me everything`
    - Add webhook
- Now, doing any activity- from pushing, to pull request GitHub would post data to our payload url, which will then be stored in `Heroku Postgres` 


## Setting up Heroku-Postgres in Heroku

1. Create an app in heroku and go to `Resources` tab, search for `Heroku Postgres` and add it to the app
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
The output would be `CREATE TABLE` if there are no issues <br />
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
app.config['SQLALCHEMY_DATABASE_URI']='<uri from postgres>'
```

# References

[Webhooks](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)
