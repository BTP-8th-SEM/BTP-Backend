from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.optionsRepository import get_all_options, get_options_by_id, create_option
from config.database import get_db
from exceptions.optionsExceptions import OptionsInfoException
from schema.optionsSchema import Options, CreateAndUpdateOptions, PaginatedOptions

router = APIRouter()

# Example of Class based view
@cbv(router)
class Answers:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/getAnswers", response_model=PaginatedOptions)
    def list_users(self, limit: int = 10, offset: int = 0):

        answers_list = get_all_options(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": answers_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/addAnswer")
    def add_user(self, answer_info: CreateAndUpdateOptions):

        try:
            answer_info = create_option(self.session, answer_info)
            return answer_info
        except OptionsInfoException as cie:
            raise HTTPException(**cie.__dict__)