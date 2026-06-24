import json
from .registry import MODULES
print(json.dumps({"atlas":"Axezent AI Verified Mathematics Atlas","module_count":len(MODULES),"global_open_problem_claims":False,"modules":MODULES}, indent=2))
