from lib.ytb_vip.ytb_info import YTB_INFO
from lib.ytb_vip.ytb_uploader import YTB_UPLOAD
from lib.ytb_vip.util import *
from lib.ixigua_spy.spy import Ixigua_Spyder
import os
import requests
from threading import Thread

class IXIGUA_YTB:
    def __init__(self, data_dir, username):
        self.data_dir = data_dir
        self.username = username
        self.parent_dir = os.path.join(data_dir, username)
        self.login_withCookie()
        self.readIxiguaIds()
    
    def login_withCookie(self):
        self.session = requests.Session()
        cookies = readCookiefromFile(os.path.join(self.parent_dir, "cookie.txt"))
        self.session.cookies.update(cookies) 
        self.ytb_info = YTB_INFO(self.session)
        self.ytb_upload = YTB_UPLOAD(self.session, self.ytb_info)

    def readIxiguaIds(self):
        with open(os.path.join(self.parent_dir, "ixigua.txt"), 'rb') as f:
            self.ixiguaIds = f.readlines()

        
        
