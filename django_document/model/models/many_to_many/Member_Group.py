from django.db import models


# 중계모델 쓰는 예제
class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=30)
    debut_date = models.DateField()
    members = models.ManyToManyField(Idol, through='Membership',through_fields=('group','idol'))

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE, related_name='membership_set')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    #recommender = models.ForeignKey(Idol, on_delete=models.SET_NULL,null=True, related_name='recommend_membership_set' )
    recommenders = models.ManyToManyField(Idol, blank=True, related_name='recommenders_membership_set', )
    date_joined = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return '({}\n {}\n {}\n)'.format(self.group.name, self.idol.name, self.is_active)
