# -*- coding: utf-8 -*-
from main.modelService import PythonBaseService
from main import log
import json
import pandas as pd
from pandas import to_datetime
import numpy as np

logger = log.getLogger(__name__)

class user_Service(PythonBaseService):

   def _preprocess(self, data):
       logger.info("begin to pre process")
       days = data["req_data"][0].split(",")
       df = pd.DataFrame(columns = ["weekday", "timeindex"])
       # generate X_test time between 5:00-20:55 in requested days
       for day in days:
           timestamp = to_datetime(day, format="%Y-%m-%d")
           df1 = pd.DataFrame({"weekday":(timestamp.dayofweek/6.0), "timeindex":(np.arange(300, 1256, 5))/(24 * 60.0)})
           df = df.append(df1, ignore_index=True)
       logger.info("end to pre process")
       return df
   
   def _postprocess(self, source_data, result_data):
       logger.info("begin to post process")
       schema = json.loads('{"wuhe_zhangheng":[1,2,3]}')
       schema["wuhe_zhangheng"] = result_data
       logger.info("end to post process")
       return json.dumps(schema)