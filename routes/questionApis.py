from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.questionRepository import get_all_questions, get_question_by_id, create_question
from config.database import get_db
from exceptions.questionExceptions import QuestionInfoException
from schema.questionSchema import Question, CreateAndUpdateQuestion, PaginatedQuestion

router = APIRouter()

# Example of Class based view
@cbv(router)
class Question:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/getQuestions", response_model=PaginatedQuestion)
    def list_questions(self, limit: int = 10, offset: int = 0):

        questions_list = get_all_questions(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": questions_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/addQuestion")
    def add_question(self, question_info: CreateAndUpdateQuestion):

        try:
            question_info = create_question(self.session, question_info)
            return question_info
        except QuestionInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular car
# @router.get("/getUser/{user_id}", response_model=User)
# def get_user_info(user_id: int, session: Session = Depends(get_db)):

#     try:
#         user_info = get_user_info_by_id(session, user_id)
#         return user_info
#     except UserInfoException as cie:
#         raise HTTPException(**cie.__dict__)


# # API to update a existing car info
# @router.put("/updateUser/{user_id}", response_model=User)
# def update_User(user_id: int, new_info: CreateAndUpdateUser, session: Session = Depends(get_db)):

#     try:
#         user_info = update_user_info(session, user_id, new_info)
#         return user_info
#     except UserInfoException as cie:
#         raise HTTPException(**cie.__dict__)


# # API to delete a car info from the data base
# @router.delete("/deleteUser/{user_id}")
# def delete_car(user_id: int, session: Session = Depends(get_db)):

#     try:
#         return delete_user_info(session, user_id)
#     except UserInfoException as cie:
#         raise HTTPException(**cie.__dict__)