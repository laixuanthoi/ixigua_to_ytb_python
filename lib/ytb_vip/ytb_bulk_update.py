from lib.ytb_vip.ytb_info import context 

class YTB_BULK_UPDATE:
    def __init__(self,session, ytb_info):
        self.session = session
        self.ytb_info = ytb_info
        self.videoIds = []

    def makeChange(self, payload):
        res = self.session.post(
            url="https://studio.youtube.com/youtubei/v1/creator/enqueue_creator_bulk_action?alt=json&key={}".format(self.ytb_info.INNERTUBE_API_KEY),
            headers = {
                "authority": "studio.youtube.com",
                "x-origin": "https://studio.youtube.com",
                "authorization": self.ytb_info.get_SAPISID_authorization(),
                "origin": "https://studio.youtube.com"
            }
            json = payload
        )

    def changePrivacy(self, videoIds, privacy):
        payload = {
            "channelId": self.ytb_info.CHANNEL_ID,
            "videoUpdate":{
                "privacyState":{
                    "privacy":"VIDEO_UPDATE_PRIVACY_SETTING_{}".formar(privacy)
                }
            },
            "videos":{
                "videoIds": videoIds
            },
            "context": context
        }
        self.makeChange(payload)
