from pyairtable import Api
from config import Config
from constants import AirTableConstants
from loguru import logger

class AirTableManager():
    def __init__(self):
        self.api = Api(api_key=Config.airtable_api_key)
        self.base_id = Config.AIRTABLE_BASE_ID

    def upsert_data(self,* , data):
        logger.info("Upserting records into Air Table.")
        table = self.api.table(base_id=self.base_id,table_name=AirTableConstants.TABLE_NAME.value)
        table.batch_upsert(
            records=[dict(fields = data)],
            key_fields = ['product id']
        )
        # table.batch_upsert(
        #     records=[{"fields":record} for record in data],
        #     key_fields=["product id"]
        # )
        logger.info("Records Upserted Successfully.")