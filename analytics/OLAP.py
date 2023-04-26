
import json
from analytics.connection import dataframes
from analytics.numpyToJSON import np_encoder
from analytics.testwise_OLAP import OLAP_Test


def run_OLAP_Test(testId: int):
    df=dataframes()
    id=0
    testOLAP=OLAP_Test(df=df,testId=testId)
    testOLAPResults=testOLAP.calculate()
    
    id=0
    searchTest=df.olap_test.query('testId==@testId')
    if len(searchTest)>0:
        id=searchTest.index()+1
    else:
        id=len(df.olap_test)+1
    testOLAPResults['id']=id
    print(dict(testOLAPResults))
    return {i:np_encoder(v) for i,v in testOLAPResults.items()}
    
    