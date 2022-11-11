import logging
from fastapi import APIRouter
#import os

from src.services.exactos_service import Exactos
from src.services.similares_service import Similares
from src.utils.common import build_error_response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


router = APIRouter()

#base_path = os.environ['basepath']

@router.get("/similares")
async def similares():
    logger.info('#START get similares')
    try:
        s = Similares()
        similares = s.get_stored_procedure()
        logger.info('#EXIT get similares')
        return similares
    except Exception as e:
        return build_error_response(e)