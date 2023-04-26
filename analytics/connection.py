import pandas as pd
import numpy as np
import mysql.connector

class dataframes:
    user=test=questions=options=responses=olap_test=olap_question=pd.DataFrame()
    def __init__(self):
        cnx = mysql.connector.connect(user='root', password='my123sql',
                              host='localhost', database='intest')

        # cnx = mysql.connector.connect(user='root', password='123456',
        #                       host='localhost', database='intest')
        
        query_user = "SELECT * FROM users"
        self.user = pd.read_sql(query_user, cnx)
        
        query_test = "SELECT * FROM test_db"
        self.test= pd.read_sql(query_test, cnx)
        
        query_questions = "SELECT * FROM questions"
        self.questions= pd.read_sql(query_questions, cnx)
        
        query_options = "SELECT * FROM mcq_options"
        self.options= pd.read_sql(query_options, cnx)
        
        query_responses = "SELECT * FROM responses"
        self.responses= pd.read_sql(query_responses, cnx)
        
        query_olap_test = "SELECT * FROM olap_test"
        self.olap_test= pd.read_sql(query_olap_test, cnx)
        
        query_olap_question = "SELECT * FROM olap_question"
        self.olap_question= pd.read_sql(query_olap_question, cnx)
        
        cnx.close()