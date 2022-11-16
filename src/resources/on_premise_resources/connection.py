import pyodbc

import logging

from src.interfaces.resources.db_connection import IDBConnection

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class RTBColRelationalDbResource(IDBConnection):
    
    def __init__(self):
        server_address = '\\'
        db_name = '\\'
        self.connection = pyodbc.connect("DRIVER={SQL Server}; SERVER="+server_address+"; DATABASE ="+db_name+"; Trusted_Connection=yes;")
        
    
    def db_connection(self, query, sp_type):
        #Metodo de conexion y consulta a RTB
        logger.info('Inicio conexión RTBCol')
        
        with self.connection as connection:
            cursor = connection.cursor()
            # OK! conexión exitosa
            logger.info('Conexion exitosa con RTBCol')
            #Inicio de consulta
            logger.info(f'Inicio ejecución de la query de {sp_type}')
            cursor.execute(query)
            #consulta exitosa
            logger.info('Ejecucion de la query Exitosa')
            sp_type_list = [ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
            return sp_type_list
