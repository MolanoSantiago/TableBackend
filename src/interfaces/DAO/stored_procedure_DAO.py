from abc import ABC
from abc import abstractmethod
import pandas as pd

class StoredProcedureDAO(ABC): 
    @abstractmethod
    def get_stored_procedure() -> pd.DataFrame:
        """Get stored procedures"""