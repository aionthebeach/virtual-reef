from . import models
import quilt3

def fetchUpcData():
	print("Get the UPC data!")
	return 0

def fetchInvertebrateData():
	quilt3.Package.install(
		"aionthebeach/reef-check",
		"s3://ai-on-the-beach",
		dest="./data"
	)
	return 0
