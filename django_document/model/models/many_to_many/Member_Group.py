from django.db import models


# 중계모델 쓰는 예제
class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=30)
    debut_date = models.DateField()
    members = models.ManyToManyField(Idol, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return '({}\n {}\n {}\n)'.format(self.group.name, self.idol.name, self.is_active)
