
import json
from analytics.connection import dataframes
from analytics.numpyToJSON import np_encoder
from analytics.testwise_OLAP import OLAP_Test
from analytics.questionwise_OLAP import OLAP_questions


def run_OLAP_Test(testId: int):
    df=dataframes()
    testOLAP=OLAP_Test(df=df,testId=testId)
    testOLAPResults=testOLAP.calculate()
    
    id=0
    searchTest=df.olap_test.query('testId==@testId')
    if len(searchTest)>0:   #if testId found in olap_test
        id=searchTest.index()   #update on existing id
    else:
        id=len(df.olap_test)+1  #create new id
    testOLAPResults['id']=id
    return {i: np_encoder(v) if type(v) not in {int, str} else v for i,v in testOLAPResults.items()}
    
def run_OLAP_Question(questionId: int):
    df=dataframes()
    questionOLAP=OLAP_questions(df)
    questionOLAPResult=questionOLAP.calculate(questionId=questionId)
    
    id=0
    searchQuestion=df.olap_question.query('questionId==@questionId')
    if len(searchQuestion)>0:   #if testId found in olap_test
        id=searchQuestion.index() #update on existing id
    else:
        id=len(df.olap_question)+1 #create new id
    
    questionOLAPResult['id']=id
    return {i: np_encoder(v) if type(v) not in {int, str} else v for i,v in questionOLAPResult.items()}
    