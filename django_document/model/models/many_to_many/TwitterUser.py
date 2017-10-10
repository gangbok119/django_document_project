from django.db import models

#재귀적 다대다 관
class TwitterUser(models.Model):
    # 자기 자신(TwitterUser ('self'))를 참조해서
    # friends필드를 MTM으로 정의
    # friends 관계가 동시에 생김... - 대칭 관계
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
