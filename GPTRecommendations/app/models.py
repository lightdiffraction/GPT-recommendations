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
    artist = str(models.CharField(max_length=100))
    question = str(models.CharField(max_length=300))
    def __init__(self, genre, question, artist):
      self.genre = genre
      self.question = question
      self.artist = artist

class QueryProcessor():
    query: Query
    prompt = ''
    response = ''
    answer = ''
    def __init__(self, query):
      self.query = query

    def process(self):

        if (self.query.artist != None and self.query.genre != None):
            self.prompt = '###Instruction### Recommend music in the'+ str(self.query.genre) +' genre that suits the description' + str(self.query.question) + 'and is made by' + str(self.query.artist) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 10 rows.'
        elif (self.query.artist == None and self.query.genre != None):
             self.prompt = '###Instruction### Recommend music in the'+ str(self.query.genre) +' genre that suits the description' + str(self.query.question) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 10 rows.'
        elif (self.query.artist != None and self.query.genre == None):
             self.prompt = '###Instruction### Recommend music that suits the description' + str(self.query.question) + 'and is made by' + str(self.query.artist) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 10 rows.'
        elif (self.query.artist == None and self.query.genre == None):
             self.prompt = '###Instruction### Recommend music that suits the description' + str(self.query.question) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 10 rows.'

    def postRequest(self):
        self.response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": self.prompt}
                ], 
            temperature = 0.9, 
            max_tokens = 400
            )
        self.answer = self.response['choices'][0]['message']['content']