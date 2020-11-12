from app import db

class Webhook_data(db.Model):
    __tablename__ = 'github_webhook_data'
    
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String())
    method = db.Column(db.String())
    headers = db.Column(db.String())
    body = db.Column(db.String())

    # db.create_all()
