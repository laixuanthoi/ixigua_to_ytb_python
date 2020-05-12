import requests

class Ixigua_Spyder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers  = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "authority": "www.ixigua.com"
        }
        
        self.signature = "ztrOnAAgEAS7K0XC317YTc7azoAAJBp"
        self.videos_user_url = "https://www.ixigua.com/home/{}/video"
        self.videos_user_api = "https://www.ixigua.com/api/videov2/author/video?_signature={}=&author_id={}&type=video&max_time=0"
        self.verify_cookie_api = "https://pc-basic.ixigua.com/api/verify?_signature={}&key={}&psm=toutiao.fe.xigua_video_web_pc"

        self.verify_cookie()
        
    def verify_cookie(self):
        cookies = self.session.get("https://www.ixigua.com/").cookies
        self.session.cookies = cookies
        self.session.get(self.verify_cookie_api.format(self.signature, cookies.get_dict()["wafid"]))
    
    def getListVideo(self, userId):
        arrVideo = []
        json = self.session.get(self.videos_user_api.format(self.signature, userId), headers={"referer": self.videos_user_url.format(userId)}).json()
        print(json)


userId = "1613708881833779"

spy = Ixigua_Spyder()
spy.getListVideo(userId)