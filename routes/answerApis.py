from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.answerRepository import get_all_answers, get_answer_by_id, create_answer
from config.database import get_db
from exceptions.answerExceptions import AnswerInfoException
from schema.answerSchema import Answer, CreateAndUpdateAnswer, PaginatedAnswerInfo

router = APIRouter()

# Example of Class based view
@cbv(router)
class Answers:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/getAnswers", response_model=PaginatedAnswerInfo)
    def list_users(self, limit: int = 10, offset: int = 0):

        answers_list = get_all_answers(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": answers_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/addAnswer")
    def add_user(self, answer_info: CreateAndUpdateAnswer):

        try:
            answer_info = create_answer(self.session, answer_info)
            return answer_info
        except AnswerInfoException as cie:
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