import pandas as pd
import pyodbc
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

server = "W03403USQL0\QAINST01"
database = "dbRTBCol"
cnxn = pyodbc.connect("DRIVER={SQL Server}; SERVER="+server +
                      "; DATABASE ="+database+"; Trusted_Connection=yes;")


def create_database_connection():
    cursor = cnxn.cursor()
    return cursor


def get_exactos():
    query = """
		WITH C AS
    	(SELECT O.object_id AS id, O.name AS Nombre, S.name AS Esquema, case O.type when 'P' then 'Stored Procedure' else ' ' end 'TipoObjeto', 
    		ROW_NUMBER() OVER	(PARTITION BY O.name ORDER BY object_id) AS ExactamenteDuplicado
    		FROM 
	    		[dbRTBCol].[sys].[objects] O
	    			LEFT JOIN [dbRTBCol].[SYS].[SCHEMAS] S ON O.schema_id = S.schema_id
    		WHERE 
    			TYPE = 'P')
		SELECT * FROM C
		WHERE ExactamenteDuplicado > 1
		"""
    df = pd.read_sql_query(sql=query, con=cnxn)
    dfdict = df.T.to_dict()
    return dfdict


# def get_similares():
#     try:
#         logger.info(f"Iniciando extracción de información")

#         cursor = cnxn.cursor()
#         cursor.execute(
#             "EXEC [dbRTBCol].[RTB].[BTG_spGeneral_ProcedimientosAlmacenadosSimilares]")

#         description = cursor.description
#         column_names = [col[0] for col in description]
#         rows = cursor.fetchall()
#         logger.info(f"Informacion extraida exitosamente")

#         if (len(rows) > 0):
#             data = [dict(zip(column_names, row)) for row in rows]
#         else:
#             data = [{column: {} for column in column_names}]

#         cursor.close()
#         return data
#     except BaseException as e:
#         logger.info(f"Error en la funcion get_similares. ERROR: {str(e)}")
#         raise


#file_name = "Procedimientos Almacenados Duplicados RTBCol.xlsx"
# df.to_excel(file_name, index = False)
# print('Dataframe successfully exported into Excel File')
