from django.db import models
from django.contrib.auth.models import User
#构建数据库

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created =models.DateTimeField(auto_now_add=True)#意味着每次用户写，系统自动生成时间，这个时间是不可改的
    datecompleted=models.DateTimeField(null=True, blank=True)#文字可以blank,但是时间按照一定的格式，如果空白就要称为null
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
#everytime we have a new model, we need to do migrations
#代码是python manage.py makemigrations
#然后是python manage.py migrate


