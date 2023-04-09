"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Query(models.Model):
    genre = models.CharField(max_length=100)
    question = models.CharField(max_length=300)
    def __init__(self, genre, question):
      self.qenre = genre
      self.question = question

class QueryProcessor():
    query: Query
    def __init__(self, query):
      self.query = query