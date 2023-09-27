
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import json 

# uniform resourse identifire
uri = "mongodb+srv://farmanmd431:farmanmd431@cluster0.bldkpl4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#create databse name and connection name
DATABASE_NAME="mlproject"
COLLECTION_NAME="waferfault"
#read the data as a dataframe
df=pd.read_csv(r"G:\EDUCATION\DS_All_project\wafer_fault_prediction\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)
#convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

# dump the data into database

client=[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
