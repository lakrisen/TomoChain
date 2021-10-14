import requests
import json 
import requests
import numpy as np 
import csv
from pandas.io.json import json_normalize 
import pandas as pd 

# Make requests to get data for all masternodes 
payloadMN = {'limit' : 2}
r1 = requests.get(url='https://master.tomochain.com/api/candidates/masternodes').json()
MN_data = r1['items']

# Save response into datagrame 
MN_DF = pd.DataFrame(MN_data)
print(MN_DF.loc[[0]])

Voter_data = []
V_DF = pd.DataFrame()
MN_total = len(MN_DF.index)

for x in range(MN_total):
    #print(x)
    r2 = requests.get(url='https://master.tomochain.com/api/candidates/'+ MN_DF['candidate'][x] +'/voters').json()
    loop_DF = pd.DataFrame(r2['items'])
   # print(loop_DF.head())
   # V_DF = V_DF.append(MN_DF.loc[[x]], ignore_index = True) #append masternode data to dataframe to 
    V_DF = V_DF.append(loop_DF, ignore_index = True)
    
   # print(V_DF.head())
    


#V_DF = pd.DataFrame(Voter_data)
print(V_DF.head())
V_DF.to_csv('MasterNode_data/New_Voter_data_updated.csv')