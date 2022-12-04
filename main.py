import argparse
import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import (
    Schoolkid, Mark, Lesson, Commendation, Chastisement, Subject
)


Commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]


def fix_marks(schoolkid):
    fixed_bad_marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__in=[1, 2, 3]
    ).update(points=5)
    return fixed_bad_marks


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    return chastisements.delete()


def create_commendation(schoolkid, subject, text):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
    ).order_by('?')
    lesson = lessons.first()
    commendation = Commendation.objects.create(
        text=text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
    return commendation


def create_parser():
    parser = argparse.ArgumentParser(
        description=
        'Let\'s fix the karma in the diary'
    )
    parser.add_argument(
        'schoolkid_and_subject',
        help=
        'Enter the command in console: '
        '$ python main.py schoolkid_and_subject {Фролов Иван Математика 6 А}. '
        'Enter the last name and first name of the student, '
        'the subject for which you want to receive praise from the teacher, '
        'as well as the klass number and the letter in which he studies.'
        'For example: Фролов Иван Математика 6 А',
        nargs='+',
        type=str,
        default=None,
    )
    parser.add_argument('year',
                        type=str,
                        default=None)
    parser.add_argument('group_letter',
                        type=str,
                        default=None)
    return parser


def main():
    parser = create_parser()
    schoolkid_name = ' '.join(parser.parse_args().schoolkid_and_subject[1:3])
    subject = ' '.join(parser.parse_args().schoolkid_and_subject[3:])
    year_of_study = parser.parse_args().year
    group_letter = parser.parse_args().group_letter
    text = random.choice(Commendations)
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=schoolkid_name,
            year_of_study=year_of_study,
            group_letter=group_letter
        )
        print(f'Исправлено оценок - {fix_marks(schoolkid)}')
        print(f'Удалено замечаний - {remove_chastisements(schoolkid)}')
        print(f'Добавлена похвала от учителя - '
              f'{(create_commendation(schoolkid, subject, text)).text}')
    except Schoolkid.DoesNotExist:
        print(f'Не нашёл ученика {schoolkid_name} '
              f'в классе {year_of_study}{group_letter}')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Несколько учеников {schoolkid_name} '
              f'в классе {year_of_study}{group_letter}')


if __name__ == '__main__':

    main()