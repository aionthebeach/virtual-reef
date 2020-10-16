from . import models
import quilt3
import os

def fetchUpcData():
	print("Get the UPC data!")
	return 0

def fetchInvertebrateData():
	p = quilt3.Package.browse("aionthebeach/reef-check", "s3://ai-on-the-beach")
	dataframe = p['invert.parquet']()
	return dataframe
