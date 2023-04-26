
from analytics.connection import dataframes

#analyzes one question by its ID
class OLAP_questions:
    df:dataframes
    result={'id': 0, 'questionId':0, 'maxMarks':0, 'highestMarks':0, 'lowestMarks':0,
             'avgMarks':0, 'topic': ''}
    testId:int
    
    #maps dataframes created 
    def __init__(self, df:dataframes):
        self.df=df

        
    #calculates analysis for a particular question by questionId
    def calculate(self,questionId:int):
        responses=self.df.responses.query('questionId==@questionId')
        question=self.df.questions.query('id==@questionId')
        self.result['questionId']=questionId
        self.result['topic']=question['topic'].iloc[0]
        self.result['maxMarks']=question['maxMarks'].iloc[0]
        self.result['highestMarks']=responses['obtainedMarks'].max()
        self.result['lowestMarks']=responses['obtainedMarks'].min()
        self.result['avgMarks']=responses['obtainedMarks'].mean()

        return self.result