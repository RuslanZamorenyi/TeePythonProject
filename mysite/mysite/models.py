from django.db import models

class Room(models.Model):
    number_desk = models.IntegerField(default=0)
    room_name = models.TextField(blank=True, null=True)
    class_room_number = models.IntegerField(default=1)


    def __str__(self):
        return self.number_desk, self.room_name, self.class_room_number


class Pupil(models.Model):
    name = models.TextField()
    surname = models.TextField()
    number_class = models.IntegerField(default=1)
    class_room_number = models.IntegerField(Room)

    def __str__(self):
        return self.name, self.surname, self.numder_class, self.class_room_numder


class Teacher(models.Model):
    name = models.TextField()
    surname = models.TextField()
    name_subject = models.TextField()
    class_teacher = models.IntegerField(default=1)
    class_room_numder = models.OneToOneField(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.surname, self.name_subject, self.class_teacher, self.class_room_numder







