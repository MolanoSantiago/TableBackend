import logging
from re import U

from src.resources.on_premise_resources.connection import RTBColRelationalDbResource
from src.interfaces.DAO.stored_procedure_DAO import StoredProcedureDAO

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Exactos(StoredProcedureDAO):
    def get_stored_procedure(self):
        #Metodo para obtener procedimientos almacenados exactos de bd ods
        logger.info('#START de petición de datos de procedimientos almacenados exactos desde el Data Access Object')
        query = """
		        WITH C AS
    	        (SELECT O.object_id AS id, O.name AS Nombre, S.name AS Esquema, 
    		        ROW_NUMBER() OVER	(PARTITION BY O.name ORDER BY object_id) AS ExactamenteDuplicado
    		    FROM 
	    		    [dbRTBCol].[sys].[objects] O
	    			    LEFT JOIN [dbRTBCol].[SYS].[SCHEMAS] S ON O.schema_id = S.schema_id
    		    WHERE 
    			    TYPE = 'P')
		        SELECT * FROM C
		            WHERE ExactamenteDuplicado > 1
		        """
        rtbcol_db_resource = RTBColRelationalDbResource()
        return rtbcol_db_resource.db_connection(query,'Procedimientos Almacenados Exactos')