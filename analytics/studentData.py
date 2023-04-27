import pandas as pd
from analytics.connection import dataframes
from analytics.questionwise_OLAP import OLAP_questions
from analytics.testwise_OLAP import OLAP_Test


#analyzes test scores wrt topics
class studentAnalysis:
    testId:int
    df:dataframes
    def __init__(self,df:dataframes) -> None:
        self.df=df
    
    #provides overall analysis of test wrt student's total score    
    def getTestData(self, testId:int, studentId: int):
        olapTest=OLAP_Test(df=self.df,testId=testId)
        results=olapTest.calculate()
        responses=self.df.responses.query('testId==@testId & userId==@studentId')
        results['studentId']=studentId
        results['totalMarksObtained']=responses['obtainedMarks'].sum()
        return results
    
    #provides analysis of particular question wrt student's response to that question
    def getQuestionData(self, testId:int, studentId: int, questionId: int):
        olapq=OLAP_questions(df=self.df)
        result=olapq.calculate(questionId=questionId)
        response=self.df.responses.query('testId==@testId & userId==@studentId & questionId==@questionId')
        print("\nsize:",response.size,"\n")
        result['obtainedMarks']=response['obtainedMarks'].iloc[0]
        return result
    
    #provides list of students that appeared in given Test
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
    
    #provides topic-wise analysis of the Test wrt student's responses
    def getTopicAnalysis(self, testId:int, userId:int):
        questions = self.df.questions.query('testId==@testId')
        responses = self.df.responses.query('testId==@testId')
        topics=questions['topic'].unique()
        
        def data(topic:str,averageMarks:float,yourMarks:int,highestMarks:int,lowestMarks:int):
            body={}
            body['topic']=topic
            body['averageMarks']=averageMarks
            body['yourMarks']=yourMarks
            body['highestMarks']=highestMarks
            body['lowestMarks']=lowestMarks
            return body

        merged_df = questions.merge(responses, left_on='id', right_on='questionId')
        results=[]
        
        merged_df = pd.merge(questions, responses, left_on='id', right_on='questionId')

        user_marks_sum = merged_df.groupby(['topic', 'userId'])['obtainedMarks'].agg('sum').reset_index()
        most_marks_by_user = user_marks_sum.groupby('topic').agg('max').reset_index()
        avg_marks_by_topic = merged_df.groupby('topic')['obtainedMarks'].agg('mean').reset_index()
        least_marks_by_user = user_marks_sum.groupby('topic').agg('min').reset_index()
        
        for topic in topics:
            yourMarks=user_marks_sum.query('topic==@topic & userId==@userId')['obtainedMarks'].iloc[0]
            highestMarks=most_marks_by_user.query('topic==@topic')['obtainedMarks'].iloc[0]
            averageMarks=avg_marks_by_topic.query('topic==@topic')['obtainedMarks'].iloc[0]
            lowestMarks=least_marks_by_user.query('topic==@topic')['obtainedMarks'].iloc[0]
            results.append(data(topic=topic,averageMarks=averageMarks,yourMarks=yourMarks,highestMarks=highestMarks,lowestMarks=lowestMarks))
        return results