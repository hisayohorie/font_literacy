#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "font_literacy.settings")
import django
django.setup()
from quiz.models import Character

import xml.etree.ElementTree as ET
import json 

filename = 'data/JMdict_e'

tree = ET.parse(filename)
root = tree.getroot()

json_data = []
words_json = []
char_occurs_json = []
word_count = 0
char_count = 0



for word in root.iter('reb'):
  save = True

  fields = {"learned": False}

  word_instance = {"model": "quiz.word", "pk": word_count, "fields": fields}

  for i, c in enumerate(list(word.text)):
    char_count += 1

    matches = Character.objects.filter(value=c)
    if len(matches) > 0:
      char = matches[0]
      fields = {"position": i, "character": char.pk, "word": word_count}
      char_occur = { "model": "quiz.CharacterOccurrence", "pk": char_count, "fields": fields}
      char_occurs_json.append(char_occur)
    else:
      save = False
      break

  if save:
    words_json.append(word_instance)
    word_count += 1



json_data = words_json + char_occurs_json
print json.dumps(json_data)
