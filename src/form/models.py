from django.db import models
from django.utils import timezone

class Doctor(models.Model):
	name =models.CharField(max_length=20)
	Email =models.CharField(max_length=20)
	content =models.TextField()
	content1 =models.TextField(blank=True)
	date =models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}'.format(self.name,self.id)
class Perasitamol(models.Model):
	m_name =models.CharField(max_length=20)
	company =models.CharField(max_length=20)
	price =models.TextField()
	date =models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}'.format(self.m_name,self.id)
class Ketorolac(models.Model):
	m_name =models.CharField(max_length=20)
	company =models.CharField(max_length=30)
	price =models.TextField()
	date =models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}'.format(self.m_name,self.id)
class Fexofenadine(models.Model):
	m_name =models.CharField(max_length=20)
	company =models.CharField(max_length=30)
	price =models.TextField()
	date =models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}'.format(self.m_name,self.id)
class Ceftriaxone(models.Model):
	m_name =models.CharField(max_length=20)
	company =models.CharField(max_length=30)
	price =models.TextField()
	date =models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}'.format(self.m_name,self.id)
# from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)