from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.optionsRepository import get_all_answers, get_answer_by_id, create_answer
from config.database import get_db
from exceptions.optionsExceptions import AnswerInfoException
from schema.optionsSchema import Answer, CreateAndUpdateAnswer, PaginatedAnswerInfo

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