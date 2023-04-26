from analytics.connection import dataframes
from analytics.questionwise_OLAP import OLAP_questions
from analytics.testwise_OLAP import OLAP_Test


#analyzes test scores wrt topics
class studentAnalysis:
    testId:int
    df:dataframes
    def __init__(self,df:dataframes) -> None:
        self.df=df
        
    def getTestData(self, testId:int, studentId: int):
        olapTest=OLAP_Test(df=self.df,testId=testId)
        results=olapTest.calculate()
        responses=self.df.responses.query('testId==@testId & userId==@studentId')
        results['studentId']=studentId
        results['totalMarksObtained']=responses['obtainedMarks'].sum()
        return results
    
    def getQuestionData(self, testId:int, studentId: int, questionId: int):
        olapq=OLAP_questions(df=self.df,testId=testId)
        result=olapq.calculate(questionId=questionId)
        response=self.df.responses.query('testId==@testId & userId==@studentId & questionId==@questionId')
        result['obtainedMarks']=response['obtainedMarks'].iloc[0]
        return result
    
    def getStudents(self,testId:int):
        responses=self.df.responses.query('testId==@testId')
        userIdList=responses.userId.unique()
        results=[]
        for id in userIdList:
            data={}
            user=self.df.user.query('id==@id').iloc[0]
            data['userId']=id
            data['firstName']=user['firstName']
            data['lastName']=user['lastName']
            data['obtainedMarks']=self.getTestData(testId=testId,studentId=id)['totalMarksObtained']
            results.append(data)
        return results