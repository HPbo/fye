#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
	name = models.CharField(max_length=10,verbose_name='name')
	age = models.IntegerField(verbose_name="age")
	gender = models.BooleanField(default=0,verbose_name="gender")
	class Meta:
		verbose_name="用户信息"
		verbose_name_plural=verbose_name
	def __unicode__(self):
		return self.name
