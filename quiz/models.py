from __future__ import unicode_literals

from django.db import models

# Create your models here.
class WritingSystem(models.Model):
    name = models.CharField(max_length=50)

class Character(models.Model):
    value = models.CharField(max_length=50)
    writing_system = models.ForeignKey(WritingSystem, on_delete=models.CASCADE)

class CharacterOccurrence(models.Model):
    position = models.IntegerField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

class Word(models.Model):
    english_translation = models.CharField(max_length=200)
    learned = models.BooleanField(default=False)

class Font(models.Model):
    name = models.CharField(max_length=50)
    source = models.CharField(max_length=200)

class Question(models.Model):
    font = models.ForeignKey(Font, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

class Guess(models.Model):
    time = models.DateTimeField()
    question = models.ForeignKey(Question, max_length=50)

class GuessedCharacter(models.Model):
    position = models.IntegerField()
    guess = models.ForeignKey(Guess, on_delete=models.CASCADE)
