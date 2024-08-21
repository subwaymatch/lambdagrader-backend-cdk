import requests
import numpy as np
import json

def handler(event, context):
    return json.dumps(np.array([1, 2, 3, 4, 5]).sum())
    # return "Hello Lambda!"