from connection import dataframes
class OLAP_Test:
    df:dataframes
    results={'id': 0, 'testId':0, 'totalAppeared':0, 'maxMarks':0, 'highestMarks':0, 'lowestMarks':0,
             'avgMarks':0, 'noOfPassed':0, 'noOfFailed':0, 'lastUpdated': ''}
    testId=0
    
    def __init__(self, df: dataframes, testId: int) -> None:
        self.df=df
        self.testId=testId
        
        
    def calculate(self):
        
        responses=self.df.responses.query('testId==@self.testId')
        test=self.df.test.query('id==@self.testId')
        
        def setTotalAppeared():
            self.results['totalAppeared']=len(responses['userId'].unique())
        
        def setMaxMarks():
            mm=test['maxMarks'].loc[0]
            self.results['maxMarks']=mm
        
        def setHighestMarks():
            max_score = responses.groupby('userId')['obtainedMarks'].sum().max()
            self.results['highestMarks']=max_score
            
        def setLowestMarks():
            min_score = responses.groupby('userId')['obtainedMarks'].sum().min()
            self.results['lowestMarks']=min_score
        
        def setAvgMarks():
            average_marks = responses.groupby('userId')['obtainedMarks'].sum().mean()
            self.results['avgMarks']=average_marks
        
        def setNoOfPassedandFailed():
            passMarks=test.passMarks.loc[0]
            passed=(responses.groupby('userId')['obtainedMarks'].sum() >= passMarks).sum()
            self.results['noOfPassed']=passed
            self.results['noOfFailed']=self.results['totalAppeared']-passed
        setTotalAppeared()
        setMaxMarks()
        setHighestMarks()
        setLowestMarks()
        setAvgMarks()
        setNoOfPassedandFailed()
        return self.results