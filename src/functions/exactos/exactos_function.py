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

@router.get("/exactos")
async def exactos():
    logger.info('#START get exactos')
    try:
        e = Exactos()
        exactos = e.get_stored_procedure()
        logger.info('#EXIT get exactos')
        return exactos
    except Exception as e:
        return build_error_response(e)