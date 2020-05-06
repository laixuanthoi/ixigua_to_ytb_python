import json, base64, os

def getImageBase64(path):
    with open(path, 'rb') as f:
        thumb_base64 = base64.b64encode(f.read()).decode('utf-8')
    return thumb_base64

def readCookiefromFile(path):
    with open(path) as f:
        obj = json.load(f)
    cookies_dict = {}
    for o in obj:
        cookies_dict.update({
            o["name"]: o["value"]
        })
    return cookies_dict

def getAccountList(accountPath):
    arr = []
    for dire in os.listdir(accountPath):
        if os.path.isdir(os.path.join(accountPath, dire)):
            arr.append(dire)
    return arr
