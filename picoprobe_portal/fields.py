import os
from urllib.parse import urlsplit, urlunsplit, urlencode
import copy
import re

def title(result):  
    if "project_metadata" in result[0]:
        t = result[0]["project_metadata"]
        if not ("experiment" in t):
            """The title for this Globus Search subject"""
            return result[0]["dc"]["titles"][0]["title"]
        return result[0]["project_metadata"]["experiment"]  
    return result[0]["experiment"]
    
