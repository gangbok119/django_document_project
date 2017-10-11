from django.db import models

__all__ = (
    'Manufacturer', 'Car', 'User',

)


class Manufacturer(models.Model):
    # ...
    name = models.CharField(max_length=40)
    pass

    def __str__(self):
        return ('브랜드명 : {}'.format(self.name))


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return ('브랜드명 : {}, 차종 : {}'.format(self.manufacturer.name, self.name))


class User(models.Model):
    name = models.CharField(max_length=30)

    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.teacher and self.pk == self.teacher.pk:
            self.teacher=None
        super(User, self).save(*args,**kwargs)



    def __str__(self):
        return ('이름 : {}'.format(self.name))
