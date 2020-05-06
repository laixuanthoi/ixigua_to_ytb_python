import requests

session = requests.Session()


class Ixigua_Spyder:
    def __init__(self):
        self.session = requests.Session()
        cookie = session.get("https://www.ixigua.com/").cookies
        print(cookie)

spy = Ixigua_Spyder()