from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    #顯示文章標題
    title   =models.CharField(max_length=200)
    #文章網址
    slug    =models.CharField(max_length=200)
    #文章內容
    body    =models.TextField()
    #本文發表時間
    pub_date=models.DateTimeField(default=timezone.now)
    class Meta:
        #指定文章要顯示的順序
        ordering=('-pub_date',)
    
    def __unicode__(self):
        return self.title