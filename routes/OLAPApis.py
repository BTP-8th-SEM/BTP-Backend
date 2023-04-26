from fastapi import APIRouter
from analytics.OLAP import run_OLAP_Test

router = APIRouter()
        
@router.get("/getAnalysisTestById/{id}", tags=["OLAP"])
def get_user_by_email(id: int):
   return run_OLAP_Test(id)
