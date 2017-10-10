from django.db import models


#재귀적 다대다 관계 / 대칭적관계 false
class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symmetrical = False 옵션으로
    # 자기자신을 참조하는 following 필드 생성
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name