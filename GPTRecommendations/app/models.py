import os
from urllib import response
import openai
openai.organization = "org-pbKlOp3rGztChAWCyGgJjxSQ"
#openai.api_key = os.getenv("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")
openai.api_key = "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"
openai.Model.list()

"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Query(models.Model):
    genre = str(models.CharField(max_length=100))
    question = str(models.CharField(max_length=300))
    def __init__(self, genre, question):
      self.qenre = genre
      self.question = question

class QueryProcessor():
    query: Query
    prompt = ''
    response = ''
    answer = ''
    def __init__(self, query):
      self.query = query
      self.query.genre = query.genre
      self.query.question = query.question

    def process(self):
        self.prompt = 'Can you please recommend music of the following genre: "' + str(self.query.genre) + '" with the following description: "' + str(self.query.question) + '"'

    def postRequest(self):
        self.response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": self.prompt}
                ], 
            temperature = 0.9, 
            max_tokens = 50
            )
        self.answer = self.response['choices'][0]['message']['content']