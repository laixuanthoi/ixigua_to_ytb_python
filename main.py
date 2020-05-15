from lib.ytb_vip.ytb_uploader import *
from lib.ytb_vip.ytb_info import *
from lib.ixigua_spy.spy import Ixigua_Spyder
from threading import Thread

DATA_DIR = "data"

def getAccountList(parent_dir):
    arr = []
    for dire in os.listdir(parent_dir):
        if os.path.isdir(os.path.join(parent_dir, dire)):
            arr.append(dire)
    return arr

def spyder_ixigua():
    ixigua_spyder = Ixigua_Spyder()
    ixigua_spyder.getListVideo

def main():
    accountList = getAccountList(DATA_DIR)
    spy_thread = Thread(target=spyder_ixigua)


if __name__ == "__main__":
    main()