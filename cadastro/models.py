#coding:utf-8
from django.db import models

# Create your models here.


SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')
	
]

class Cadastro (models.Model):
	
	Nome = models.CharField('Nome',max_length=100)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES)
	Cidade = models.CharField('Cidade',max_length=100)
	Bairro = models.CharField('Bairro',max_length=100)
	Endereco = models.CharField('Endereco',max_length=100)
	Numero = models.IntegerField('Numero')
	Telefone = models.CharField('Telefone',max_length=15)
	Celular = models.CharField('Celular',max_length=15)
	Email = models.CharField('Email',max_length=100)
	
	
	def  __unicode__(self):
		return self.Nome
	
