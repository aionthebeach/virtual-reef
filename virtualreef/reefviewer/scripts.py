from . import models
import quilt3
import pandas as pd

def fetchUpcData():
	print("Get the UPC data!")
	quilt3.Package.install( "aionthebeach/reef-check",
    registry="s3://ai-on-the-beach",
    dest="./data/")
	df = pd.read_parquet("./data/upc.parquet")
	return df
