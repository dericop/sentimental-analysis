from django.db import models

class user_facebook(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	SEX = (
			(MALE, 'Male'),
			(FEMALE, 'Female'),
		)

	id_user = models.CharField(max_length = 200, blank = False, primary_key=True)
	email = models.EmailField(max_length = 70, blank = True, null = True)
	about_me = models.CharField(max_length = 200, blank = True, null = True)
	birthday = models.DateField( blank = True, null = True)
	city = models.CharField( max_length = 100, blank = True, null = True)
	country = models.CharField(max_length = 30, blank = True, null = True)
	devices = models.CharField(max_length = 400, blank = True, null = True) # cambiar
	education = models.CharField(max_length = 400, blank = True, null = True) # cambiar
	inspirational_people = models.CharField(max_length = 400, blank = True, null = True) # cambiar
	friend_count = models.IntegerField(default=0, blank = True, null = True) 
	age_range_init = models.IntegerField(default=0, blank = True, null = True) 
	age_range_end = models.IntegerField(default=0, blank = True, null = True) 
	sex = models.CharField(max_length = 1, choices = SEX, default = MALE, blank = True, null = True)
	books = models.CharField(max_length = 200, blank = True, null = True)
	sports = models.CharField(max_length = 600,blank = True, null = True)
	music = models.CharField(max_length = 200, blank = True, null = True)
	locale = models.CharField(max_length = 200,blank = True, null = True)
	religion = models.CharField(max_length = 200, blank = True, null = True)
	movies = models.CharField(max_length = 200, blank = True, null = True)
	tv = models.CharField(max_length = 200, blank = True, null = True)

	def __unicode__(self):
		return self.id_user

class likes(models.Model):
	from_id = models.ForeignKey(user_facebook)
	page_name = models.CharField(max_length = 200, blank = True)

	def __unicode__(self):
		return "Id: "+self.from_id+" Nombre: "+self.page_name

class page(models.Model):
	id_page = models.CharField(max_length = 200, blank = False, primary_key = True)
	about_me = models.CharField(max_length = 200, blank = True)
	categories = models.CharField(max_length = 600, blank = True)
	culinary_team = models.CharField(max_length = 200, blank = True)
	attire = models.CharField(max_length = 200, blank = True)
	general_manager = models.CharField(max_length = 200, blank = True)
	hour_init = models.CharField(max_length = 20, blank = True)
	hour_end = models.CharField(max_length = 20, blank = True)
	user_name = models.CharField(max_length = 100, blank = True)
	products = models.CharField(max_length = 200, blank = True)
	keywords = models.CharField(max_length = 200, blank = True)
	page_type = models.CharField(max_length = 200, blank = True)
	range_price = models.CharField(max_length = 100, blank = True)

	def __unicode__(self):
		return self.id_page

class message(models.Model):
	from_id = models.ForeignKey(user_facebook)
	count_likes = models.IntegerField(default=0)
	text = models.TextField(blank = False)
	time = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.text


class interest(models.Model):
	name = models.CharField(max_length = 100)
	id_user = models.ManyToManyField(user_facebook)

	def __unicode__(self):
		return self.name

class word(models.Model):
	POSITIVE = 'PO'
	NEGATIVE = 'NE'
	NEUTRAL  = 'NT'
	NONE  = 'NN'

	POLARITY = (
		(POSITIVE, 'Positive'),
    	(NEGATIVE, 'Negative'),
    	(NEUTRAL, 'Neutral'),
    	(NONE, 'None'),
	)

	name = models.CharField(max_length = 200, blank = False)
	polarity = models.CharField(max_length = 2, choices= POLARITY, blank = True, null = True)
	gram_root = models.CharField(max_length = 200, blank = True, null = True)

	def __unicode__(self):
		return "Palabra: "+self.name+ " Polaridad: "+self.polarity

class polarity(models.Model):
	POSITIVE = 'PO'
	NEGATIVE = 'NE'
	NEUTRAL  = 'NT'
	POLARITY = (
		(POSITIVE, 'Positive'),
    	(NEGATIVE, 'Negative'),
    	(NEUTRAL, 'Neutral'),
	)

	id_message = models.ForeignKey(message)
	per_positive = models.FloatField()
	per_negative = models.FloatField()
	per_neutral = models.FloatField()
	classification = models.CharField(max_length = 2, choices = POLARITY, default = NEUTRAL)

	def __unicode__(self):
		return "Id Mensaje: "+self.id_message+ "Clasificacion "+self.classification

class commentsClassified(models.Model):
	POSITIVE = 'PO'
	NEGATIVE = 'NE'
	NEUTRAL  = 'NT'
	NONE  = 'NN'

	POLARITY = (
		(POSITIVE, 'Positive'),
    	(NEGATIVE, 'Negative'),
    	(NEUTRAL, 'Neutral'),
    	(NONE, 'None'),
	)
	from_message_id= models.ForeignKey(message)
	auto_classification = models.CharField(max_length = 2, choices = POLARITY, default = NEUTRAL)
	user_classification = models.CharField(max_length = 2, choices = POLARITY, default = NEUTRAL,  blank = True, null = True)
	text = models.TextField(blank = False, default = "")
	id_page = models.CharField(max_length = 200, blank = False)

	def __unicode__(self):
		return self.id_page










	

