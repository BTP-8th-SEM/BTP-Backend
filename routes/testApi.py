from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from repository.testRepository import *
from config.database import get_db
from exceptions.optionsExceptions import OptionsInfoException
from schema.testSchema import Test, CreateAndUpdateTest, PaginatedTest

router = APIRouter()

# Example of Class based view
@cbv(router)
class Answers:
    session: Session = Depends(get_db)

    # API to get the list of car info
    @router.get("/getTests", response_model=PaginatedTest)
    def list_users(self, limit: int = 10, offset: int = 0):

        test_list = get_all_tests(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": test_list}

        return response

    # API endpoint to add a car info to the database
    @router.post("/createTest")
    def create_test(self, test_info: CreateAndUpdateTest):

        try:
            test_info = create_test(self.session, test_info)
            return test_info
        except OptionsInfoException as cie:
            raise HTTPException(**cie.__dict__)