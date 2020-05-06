import re, datetime, requests, hashlib
#get info from youtube studio page content
context = {
    "client": {
        "clientName": 62,
        "clientVersion": "1.20200420.03.00",
        "hl": "en",
        "gl": "US",
        "experimentsToken": ""
    },
    "request": {
        "returnLogEntry": True,
        "internalExperimentFlags": [
            {
            "key": "force_live_chat_merchandise_upsell",
            "value": "false"
            },
            {
            "key": "force_route_delete_playlist_to_outertube",
            "value": "false"
            },
            {
            "key": "force_route_innertube_shopping_settings_to_outertube",
            "value": "true"
            }
            ]
    },
    "clientScreenNonce": "MC42MjI0MTk4NzkxNjE2NTU4"
} 

class YTB_INFO:
    def __init__(self, session):
        self.session = session
        self.pageContent = self.session.get(
            url = "https://studio.youtube.com/").text
        self.groupRegex = re.findall('''[^:\"]+''', self.pageContent)
        self.INNERTUBE_API_KEY = self.groupRegex[self.groupRegex.index("INNERTUBE_API_KEY")+1]
        self.CHANNEL_ID = self.groupRegex[self.groupRegex.index("CHANNEL_ID")+1]

    def get_SAPISID_authorization(self):
        x_origin = "https://studio.youtube.com"
        time_stamp = str(int(datetime.datetime.now().timestamp()))
        hash_str = "{} {} {}".format(time_stamp, self.session.cookies.get_dict()["SAPISID"], x_origin).encode('utf-8')
        hexdigit = hashlib.sha1(hash_str).hexdigest()
        code = "SAPISIDHASH {}_{}".format(time_stamp, hexdigit)
        return code
    


