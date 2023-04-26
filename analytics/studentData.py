from analytics.connection import dataframes
from analytics.questionwise_OLAP import OLAP_questions
from analytics.testwise_OLAP import OLAP_Test


#analyzes test scores wrt topics
class studentAnalysis:
    testId:int
    df:dataframes
    def __init__(self,df:dataframes) -> None:
        self.df=df
        
    #returns overall analysis of the student's test
    def getTestData(self, testId:int, studentId: int):
        olapTest=OLAP_Test(df=self.df,testId=testId)
        results=olapTest.calculate()
        responses=self.df.responses.query('testId==@testId & userId==@studentId')
        results['studentId']=studentId
        results['totalMarksObtained']=responses['obtainedMarks'].sum()
        return results
    
    #returns questionId-based analysis of student's responses
    def getQuestionData(self, testId:int, studentId: int, questionId: int):
        olapq=OLAP_questions(df=self.df,testId=testId)
        result=olapq.calculate(questionId=questionId)
        response=self.df.responses.query('testId==@testId & userId==@studentId & questionId==@questionId')
        result['obtainedMarks']=response['obtainedMarks'].iloc[0]
        return result