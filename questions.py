import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "font_literacy.settings")
import django
django.setup()
from quiz.models import Font, Word
import json

json_data = []
count = 1

for word in Word.objects.all():
  for font in Font.objects.all():
    fields = {"word": word.pk, "font": font.pk}
    question = {"model": "quiz.question", "pk": count, "fields": fields}
    count += 1
    json_data.append(question)
    


print json.dumps(json_data)
