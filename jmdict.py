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
word_count = 0
char_count = 0

for word in root.iter('reb'):

  word_count += 1
  fields = {"learned": False}

  word_instance = {"model": "quiz.word", "pk": word_count, "fields": fields}
  json_data.append(word_instance)

  for i, c in enumerate(list(word.text)):
    char_count += 1

    char = Character.get(value=c)
    fields = {"position": i, "character": char, "word": word_count}
    char_occur = { "model": "quiz.CharacterOccurrence", "pk": char_count, "fields": fields}
    json_data.append(char_occur)



print json.dumps(json_data)
