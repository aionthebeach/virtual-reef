from django.db import models

# Create your models here.
class ReefSite(models.Model):
	"""
	ReefSite

	Discussion:
	Top level object for survey sites.
	Uniquely keyed by the `site` field in the raw data.

	"""
	name = models.CharField(max_length=200)
	region = models.CharField(max_length=200)

	latitude = models.DecimalField(default=0, max_digits=10, decimal_places=7)
	longitude = models.DecimalField(default=0, max_digits=10, decimal_places=7)


	def __init__(self, arg):
		super(ReefSite, self).__init__()
		self.arg = arg
		

class ReefSurvey(models.Model):
	"""
	ReefSurvey

	Discussion:
	Top level model object for Reef Check Surveys. 
	Represents a single survey at a site on a particular date.
	"""
	surveySite = models.ForeignKey(ReefSite, on_delete=models.CASCADE)
	surveyDate = models.DateTimeField('Survey Date')

	def __init__(self, arg):
		super(ReefSurvey, self).__init__()
		self.arg = arg

class ReefTransect(models.Model):
	"""
	ReefTransect

	Discussion:
	Represents a single transect line on a specific survey.
	"""
	survey = models.ForeignKey(ReefSurvey, on_delete=models.CASCADE)

	visibility = models.DecimalField(default=0, max_digits=10, decimal_places=5)
	heading = models.DecimalField(default=0, max_digits=10, decimal_places=5)
	depth = models.DecimalField(default=0, max_digits=10, decimal_places=5)
	temp = models.DecimalField(default=0, max_digits=10, decimal_places=5)

	def __init__(self, arg):
		super(ReefTransect, self).__init__()
		self.arg = arg
		

class SurveyUPC(models.Model):
	"""
	SurveyUPC
	Uniform Point Contact Survey
	
	Discussion:
	UPC surveys have information about Cover, Substrate, and Relief. 
	All fields should default to zero. 
	The sum of all fields in a category must equal 30.

	Relief has been given codesafe names for size categories:
	small: 0-10cm
	medium: 10cm-1m
	large: 1m-2m
	giant: >2m
	"""

	# Linked Survey
	models.ForeignKey(ReefTransect, on_delete=models.CASCADE)

	# Cover
	articulatedCoralline = models.IntegerField(default=0)
	brownSeaweed = models.IntegerField(default=0)
	crustoseCoralline = models.IntegerField(default=0)
	greenSeaweed = models.IntegerField(default=0)
	none = models.IntegerField(default=0)
	otherBrownSeaweed = models.IntegerField(default=0)
	redSeaweed = models.IntegerField(default=0)
	sessileInvertebrates = models.IntegerField(default=0)

	# Substrate
	bedrock = models.IntegerField(default=0)
	boulder = models.IntegerField(default=0)
	cobble = models.IntegerField(default=0)
	other = models.IntegerField(default=0)
	sand = models.IntegerField(default=0)

	# Relief
	small = models.IntegerField(default=0)
	medium = models.IntegerField(default=0)
	large = models.IntegerField(default=0)
	giant = models.IntegerField(default=0)

	def __init__(self, arg):
		super(SurveyUPC, self).__init__()
		self.arg = arg
		
class SurveyAlgae(object):
	"""
	docstring for SurveyAlgae
	"""
	
	# Linked Survey
	models.ForeignKey(ReefTransect, on_delete=models.CASCADE)

	def __init__(self, arg):
		super(SurveyAlgae, self).__init__()
		self.arg = arg

class SurveyInvertebrate(object):
	"""
	docstring for SurveyInvertebrate
	"""

	# Linked Survey
	models.ForeignKey(ReefTransect, on_delete=models.CASCADE)

	def __init__(self, arg):
		super(SurveyInvertebrate, self).__init__()
		self.arg = arg

class SurveyFish(object):
	"""
	docstring for SurveyFish
	"""

	# Linked Survey
	models.ForeignKey(ReefTransect, on_delete=models.CASCADE)

	def __init__(self, arg):
		super(SurveyFish, self).__init__()
		self.arg = arg
		