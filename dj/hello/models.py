from django.db import models


class GithubData(models.Model):
    
    path = models.TextField()
    method = models.TextField()
    headers = models.TextField()
    body = models.TextField()
