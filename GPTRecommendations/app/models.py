import os

from urllib import response
import openai
openai.organization = "org-pbKlOp3rGztChAWCyGgJjxSQ"

from configparser import ConfigParser
config = ConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), 'auth.ini');
config.sections()
config.read(configFilePath)
YOUR_API_KEY = config.get('auth', 'API_KEY')
openai.api_key = YOUR_API_KEY
openai.Model.list()

"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Music():
    music = str(models.CharField(max_length=100))
    artist = str(models.CharField(max_length=100))
    def __init__(self, music, artist):
      self.music = music
      self.artist = artist

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
    table = []
    def __init__(self, query):
      self.query = query

    def process(self):

        if (self.query.artist != None and self.query.genre != None):
            self.prompt = '###Instruction### Recommend music in the'+ str(self.query.genre) +' genre that suits the description' + str(self.query.question) + ' and is made by' + str(self.query.artist) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 9 rows.'
        elif (self.query.artist == None and self.query.genre != None):
             self.prompt = '###Instruction### Recommend music in the'+ str(self.query.genre) +' genre that suits the description' + str(self.query.question) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 9 rows.'
        elif (self.query.artist != None and self.query.genre == None):
             self.prompt = '###Instruction### Recommend music that suits the description' + str(self.query.question) + ' and is made by' + str(self.query.artist) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 9 rows.'
        elif (self.query.artist == None and self.query.genre == None):
             self.prompt = '###Instruction### Recommend music that suits the description' + str(self.query.question) + '. Format the result as a table such as "TABLE: 1.1. first music name 1.2. first music artist name 2.1. second music name 2.2. second music artist name" etc. The table should have 9 rows.'

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

    def parseRequest(self):
        self.table = []
        for i in range (1, 9):
            musicstart = self.answer.find(str(i)+'.1')
            musicend = self.answer.find(str(i)+'.2')
            if (i != 9):
                artistend = self.answer.find(str(i+1)+'.1')
            else:
                artistend = len(self.answer)-1
            self.table.append(Music(self.answer[musicstart:musicend], self.answer[musicend:artistend]))
