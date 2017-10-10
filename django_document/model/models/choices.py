from django.db import models

__all__ = (
    'Person'
)


class Person(models.Model):
    # 왼쪽이 DB에 저장, 오른쪽이 클라이언트에게 보임.
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
