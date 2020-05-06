import re, requests, json
import lib.util as util
from lib.ytb.ytb_info import YTB_INFO
from lib.ytb.ytb_uploader import YTB_UPLOAD

session = requests.Session()
cookies = util.readCookiefromFile("cookie.json")
session.cookies.update(cookies)
session.headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

ytb_info = YTB_INFO(session)
ytb_upload = YTB_UPLOAD(session, ytb_info)

videoInfo = {
    "thumbPath": "assets/2.jpg",
    "videoPath": "assets/112.mp4",
    "privacyState": "PUBLIC", #PUBLIC UNLISTED PRIVATE
    "title": "heheheheh",
    "description": "kakakakak",
    "tags": ["please", "dont", "delete", "my", "video"],
    "categoryId": 22,
    "audioLanguage": "en",
    "videoId": "",
    "playlistsIds": []
}

ytb_upload.uploadVideo(videoInfo)
print("okkkk")
print(videoInfo)
