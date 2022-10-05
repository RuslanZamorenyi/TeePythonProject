from django.http import HttpResponse

from .models import Pupil, Teacher, Room


def create_pupil(request):
    pupil = Pupil.objects.create(**{
        'name': 'Василь',
        'surname': "Al Capone",
        'number_class': 3,
        'class_room_number': 24,
    })
    pupil_1 = Pupil.objects.create(**{
        'name': 'Віталік',
        'surname': "-",
        'number_class': 4,
        'class_room_number': 4,
    })
    pupil_2 = Pupil.objects.create(**{
        'name': 'Игнат',
        'surname': "Абрамович",
        'number_class': 1,
        'class_room_number': 4,
    })

    return HttpResponse(pupil, pupil_1, pupil_2)

def create_teacher(request):
    teacher = Teacher.objects.create(**{
        'name': 'Вова',
        'surname': "Зеленский",
        'name_subject': "politics",
        'class_teacher': 9,
        'class_room_number': 10,
    })
    teacher_1 = Teacher.objects.create(**{
        'name': 'Слава',
        'surname': "Водный",
        'name_subject': "chemistry",
        'class_teacher': 1,
        'class_room_number': 2,
    })

    return HttpResponse(teacher, teacher_1)

def create_room(request):
    room = Room.objects.create(**{
        'number_desk': 1,
        'room_name': "math",
        'class_room_number': 7,
    })
    # room_1 = Room.objects.create(**{
    #     'number_desk': 3,
    #     'room_name': "chemistry",
    #     'class_room_number': 9,
    # })
    return HttpResponse(room, )

