import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import progressbar

class Ixigua_Spyder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers  = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "authority": "www.ixigua.com"
        }
        
        self.signature = "ztrOnAAgEAS7K0XC317YTc7azoAAJBp"
        self.videos_user_url = "https://www.ixigua.com/home/{}/video"
        self.videos_user_api = "https://www.ixigua.com/api/videov2/author/video?_signature={}=&author_id={}&type=video&max_time={}"
        self.verify_cookie_api = "https://pc-basic.ixigua.com/api/verify?_signature={}&key={}&psm=toutiao.fe.xigua_video_web_pc"
        self.thumb_url = "{}~tplv-crop-center:1440:810.jpg"
        self.video_url = "https://www.ixigua.com/i{}"
        self.videofk_url = "https://www.videofk.com/index-video-download/search?url={}"
        self.pbar = None
        self.verify_cookie()
        
    def verify_cookie(self):
        cookies = self.session.get("https://www.ixigua.com/").cookies
        self.session.cookies = cookies
        self.session.get(self.verify_cookie_api.format(self.signature, cookies.get_dict()["wafid"]))
    
    def getListVideo(self, userId):
        arrVideo = []
        max_time = 0
        has_more = True
        while has_more:
            obj = self.session.get(self.videos_user_api.format(self.signature, userId, max_time), headers={"referer": self.videos_user_url.format(userId)}).json()
            for item in obj["data"]["data"]:
                arrVideo.append(item)
            
            max_time = arrVideo[-1]["behot_time"]
            has_more = obj["data"]["has_more"]

        return arrVideo

    def show_download_progress(self, block_num, block_size, total_size):
        if self.pbar is None:
            self.pbar = progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()
            self.pbar = None

    def downloadVideo(self, videoId):
        if 'i' in videoId:
            videoId = videoId.replace('i','')
        url = self.video_url.format(videoId)
        api = self.videofk_url.format(url)
        html = requests.get(api).text
        soup = BeautifulSoup(html, "html.parser")
        download_link = soup.find("a", {"class": "download"})['href']
        videoName = "{}.mp4".format(videoId)
        print("Download video: {}".format(videoName))
        urlretrieve(download_link, videoName, self.show_download_progress)



# userId = "1613708881833779"
userId = "98175235867"

spy = Ixigua_Spyder()
# spy.getListVideo(userId)
spy.downloadVideo("6825810893356401156")