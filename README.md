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

## Setting up database

1. Install PostgreSQL
```
sudo apt-get install postgresql postgresql-contrib
```
2. Create a superuser for PostgreSQL
```
sudo -u postgres createuser --superuser <name_of_user>
```
```
sudo -u postgres createuser --superuser ram
```
3. Create a database using created user account
```
sudo -u <name_of_user> createdb <name_of_database>
```
```
sudo -u ram createdb github_data
```
We can access created database with created user by,
```psql -U <name_of_user> -d <name_of_database>```

```
psql -U ram -d github_data
```

this will display the database you are connected to as well as the user logged on
```
\conninfo
```
