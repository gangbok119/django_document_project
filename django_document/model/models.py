from django.db import models

# Create your models here.

class Person(models.Model):
    # 왼쪽이 DB에 저장, 오른쪽이 클라이언트에게 보임.
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)



class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

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
        return ('브랜드명 : {}, 차종 : {}'.format(self.manufacturer.name,self.name))