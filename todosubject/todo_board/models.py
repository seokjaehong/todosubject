from django.conf import settings
from django.db import models

# Create your models here.
# from user.models import User
# from ..user.models import User
# from todosubject.user.models import User

# from user.models import User
user = settings.AUTH_USER_MODEL


class ProjectCode(models.Model):
    name = models.CharField('p_name', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TodoList(models.Model):
    pcode = models.ForeignKey(ProjectCode, on_delete=models.CASCADE)
    user = models.ForeignKey(user, related_name='user_todo_list', on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=20)
    contents = models.TextField('내용', null=True, blank=True)
    is_complete = models.BooleanField('완료여부', default=False)
    end_date = models.DateField('완료일', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed=False
    #     db_table =
