import logging
from re import U

from src.resources.on_premise_resources.connection import RTBColRelationalDbResource
from src.interfaces.DAO.stored_procedure_DAO import StoredProcedureDAO

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Similares(StoredProcedureDAO):
    def get_stored_procedure(self):
        #Metodo para obtener procedimientos almacenados similares de bd ods
        logger.info('#START de petición de datos de procedimientos almacenados similares desde el Data Access Object')
        query = "EXEC [dbRTBCol].[RTB].[BTG_spGeneral_ProcedimientosAlmacenadosSimilares]"
        rtbcol_db_resource = RTBColRelationalDbResource()
        return rtbcol_db_resource.db_connection(query,'Procedimientos Almacenados Similares')