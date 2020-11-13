from app import db




class webhook_data(db.Model):
    __tablename__ = 'github_webhook_data'
    
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String())
    method = db.Column(db.String())
    headers = db.Column(db.String())
    body = db.Column(db.String())

    def __init__(self, path, method, headers, body):
        self.path = path
        self.method = method
        self.headers = headers
        self.body = body

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'path': self.path,
            'method': self.method,
            'headers,':self.headers,
            'body,':self.body,
        }