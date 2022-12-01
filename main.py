import argparse
from math import e
import os
import random

import django
from django.core.exceptions import MultipleObjectsReturned

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Lesson
from datacenter.models import Commendation
from datacenter.models import Chastisement
from datacenter.models import Subject


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


commendations = [
    'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
    'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!',
    'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!',
    'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
    'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!'
    ]


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[1, 2, 3]).all()
    for mark in bad_marks:
        # print(mark)
        mark.points = 5
        # print(mark)
        mark.save()
    return bad_marks.count()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
















































