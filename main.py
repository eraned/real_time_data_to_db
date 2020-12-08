import numpy as np
import pandas as pd
import requests
import json
import random


 url = "https://data.gov.il/api/action/datastore_search?resource_id=5e87a7a1-2f6f-41c1-8aec-7216d52a6cf6"
  url = "http://api.open-notify.org/iss-pass.json"
 JSONContent = requests.get(url).json()
 content = json.dumps(JSONContent, indent = 4, sort_keys=True)
 print(content)
 D = JSONContent['result']['records']
ds = pd.DataFrame(D)
ds.head(100)




    

