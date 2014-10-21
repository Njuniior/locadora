from django.db import models

# Create your models here.


SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

class CadastroPessoa (models.Model):
	
	Nome = model.Charfield('Nome',max_length=100)
	Sexo = model.Charfield('Sexo',max_length=2)
	Cidade = model.Charfield('Cidade',max_lenght=100)
	Bairro = model.Charfield('Bairro',max_lenght=100)
	Endereco = model.Charfield('Endereco',max_lenght=100)
	Numero = model.Charfield('Numero')
	Telefone = model.Charfield('Telefone',max_lenght=15)
	Celular = model.Charfield('Celular',max_lenght=15)
	Email = model.Charfield('Email',max_lenght=100)
	
	
	def  __unicode__(self):
		return self.Nome
	
