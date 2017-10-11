from django.db import models

__all__ = (

    'CommonInfo', 'Student', 'Teacher'
)


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 역참조 매니저를 상속시키는 방법까지
class CommonInfo(models.Model):
    school = models.ForeignKey(School, blank=True, null=True,
                               related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss",
                               )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)
