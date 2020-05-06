import os, random, json
from lib.ytb_vip.util import getImageBase64
from lib.ytb_vip.ytb_info import context

# videoInfo = {
#     "thumbPath": "",
#     "videoPath": "",
#     "privacyState": "UNLISTED", #PUBLIC UNLISTED PRIVATE
#     "title": "",
#     "description": "",
#     "tags": [],
#     "categoryId": 22,
#     "audioLanguage": "en",
#     "videoId": "",
#     "playlistsIds": []
#     "madeForKid": False
# }

class YTB_UPLOAD:
    def __init__(self, session, ytb_info):
        self.session = session
        self.ytb_info = ytb_info

    def random_innertube_studio(self):
        # frontendUploadId = "innertube_studio:1B10B4A0-D4CF-47BE-9E3A-3F6487F09054:0"
        az = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.frontendUploadId = "innertube_studio:{}{}{}{}{}{}{}{}-{}{}{}{}-{}{}{}{}-{}{}{}{}-{}{}{}{}{}{}{}{}{}{}{}{}:0".format(random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),random.choice(az),)

    
    def step_1_make_session(self, videoPath):
        file_name = str(os.path.basename(videoPath))
        file_size = str(os.path.getsize(videoPath))
        self.random_innertube_studio()
        res = self.session.post(
            url = "https://upload.youtube.com/upload/studio",
            json = {"frontendUploadId": self.frontendUploadId},
            headers = {
                "origin": "https://studio.youtube.com",
                "x-goog-upload-command": "start",
                "x-goog-upload-file-name": file_name,
                "x-goog-upload-header-content-length": file_size,
                "x-goog-upload-protocol": "resumable"
            }
        )
        upload_URI, scotty_resourceID = res.headers["X-Goog-Upload-URL"], res.headers["X-Goog-Upload-Header-Scotty-Resource-Id"]
        return upload_URI, scotty_resourceID
    
    def step_2_create_video_ids(self, scottyID, title="VIDEO_0001", privacy="UNLISTED", isDraft=False):
        payload = { 
                "channelId": self.ytb_info.CHANNEL_ID,
                "resourceId": {
                    "scottyResourceId": {
                        "id": str(scottyID)
                    }
                },
                "frontendUploadId": self.frontendUploadId,
                "initialMetadata": {
                    "title": {
                        "newTitle": str(title)
                    },
                    "privacy": {
                        "newPrivacy": str(privacy)
                    },
                    "draftState": {
                        "isDraft": isDraft
                    }
                },
                "botguardClientResponse": "u0021OTqlOhtCxp0I4_osOdJYKZ4k06HUr-ICAAAAQ1IAAAAkmQKDI7G6yg7-4B5cMW4V9WS7N0Jm-m16W8MIDyYIl5TbapP7-r-Z0dTn1e7wRgi2rdNvlJzSEDRkq5cvCsTlgA-6tDTwhNglK_egA-TwhtzUY1rF7Dyz6lkimAKrz9uRAT1gAiCmpJNn5-x5S4W1cwANLpGY1MinwZANrHdq8rWhGkAWG019YDlD0tKdFyVlu5nIx76Gm26aXcmjrjtZISZoL3N01kX0KT-v-BndeYiMfX82cGvW9Pd35hi2-4eTl--Ar_EuOTu7g5vZn_uFIjuytZ-jLN632h61rg41mLFLLOBURQB40C16djQJdxOHHh1cAvMc0GpKdZg5H1ETX0rnyvNDXls4Wpdn8fiQSgak0ekn8mMpUJxDODHQNTtb0rpbEbeMd3CFRY9DnJVIKWbsrqPgCDumsj0h2yqjOkeopGh9CwNU91imnuI2ajuQTbCsHypkL47f6VPFFZ1ohPBYgOmitt4L2IVP6SJBiZJzHTSXQ42bqX2vm3wtzTFh7sTglWjR0z23S4hLmd6muJPMU2ZxXR85evHJ-xZyiL4LgsAkh5VaX2ApPPEPIqewGdoFtvySgC8xNUe2_LrAfiUzNZlITe3CALDhKKGhSbA0voZHcupNH3VvpIGMMfPNuDKIz9tvSN26WPLc82RL-8Up8_ucGIqpklvRbrBwo1DHY1QckRkvu2qASR9DlsSFqbXTTxEkV7zG7U1De8PnJLY13pufQgoczngj4diLkJ7tJlELzbosqB2Gy8tapOLHTVxjQ0oCQNVEZd4AbvrXl4ZX3YSPpws_wsGHKYzcBOlJu-BT9RvfIPBmKzgw68sQtD7eS2cwv_tJEPz9-ZSsrY1XB34CSQ",
                "context": context
        }

        res = self.session.post(
            url="https://studio.youtube.com/youtubei/v1/upload/createvideo?alt=json&key={}".format(self.ytb_info.INNERTUBE_API_KEY),
            json= payload,
            headers = {
            "authorization": self.ytb_info.get_SAPISID_authorization(),
            "origin": "https://studio.youtube.com",
        })
        return res.json()["videoId"]

    def step_3_upload_video(self, upload_URI, videoPath):
        with open(videoPath, "rb") as finput:
            file_name = str(os.path.basename(videoPath))
            file_size = str(os.path.getsize(videoPath))
            print(file_name, file_size)
            res = self.session.post(
                url=upload_URI,
                data=finput,
                headers = {
                    "authority": "upload.youtube.com",
                    "content-length": file_size,
                    "x-goog-upload-command": "upload, finalize",
                    "x-goog-upload-file-name": file_name,
                    "x-goog-upload-offset": "0",
                    "content-type": "application/x-www-form-urlencoded;charset=utf-8",
                    "origin": "https://studio.youtube.com", 
                    "sec-fetch-site": "same-site",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                }
            )
        return res.status_code

    def step_4_update_video_infomation(self, videoInfo):
        data = {
                "encryptedVideoId": videoInfo["videoId"],
                "targetedAudience":{
                    "operation": "MDE_TARGETED_AUDIENCE_UPDATE_OPERATION_SET",
                        #"newTargetedAudience": "MDE_TARGETED_AUDIENCE_TYPE_CROSSWALK" - made for kid
                    "newTargetedAudience": "MDE_TARGETED_AUDIENCE_TYPE_ALL" # -not for kid
                    },
                "context": context
            }
        #thumbnail
        if videoInfo["thumbPath"] != "":
            data.update({
                "videoStill": {
                    "operation": "UPLOAD_CUSTOM_THUMBNAIL",
                    "image": {
                        "dataUri": "data:image/jpeg;base64,{}".format(getImageBase64(videoInfo["thumbPath"]))
                    }
                }
            })
        #title
        if videoInfo["title"] != "":
            data.update({
                "title": {
                    "newTitle": videoInfo["title"],
                    "shouldSegment": True
                }
            })

        #description
        if videoInfo["description"] != "":
            data.update({
                "description": {
                    "newDescription": videoInfo["description"],
                    "shouldSegment": True
                }
            })
        #tags
        if videoInfo["tags"] != []:
            data.update({
                "tags": {
                    "newTags": videoInfo["tags"]
                }
            })
        #privacy
        if videoInfo["privacyState"] != []:
            data.update({
                "privacyState": {
                    "newPrivacy": videoInfo["privacyState"]
                }
            })
        #category
        if videoInfo["categoryId"] != "":
            data.update({"category": {
                "newCategoryId": videoInfo["categoryId"]
                }
            })
        
        #audioLanguage
        if videoInfo["audioLanguage"] != "":
            data.update({"audioLanguage": {
                "newAudioLanguage": videoInfo["audioLanguage"]
                 }
            })
        #playlist
        if videoInfo["playlistsIds"] != []:
            data.update({"addToPlaylist": {
                "addToPlaylistIds": videoInfo["playlistsIds"], 
                "deleteFromPlaylistIds": []
             }
            })
        res = self.session.post(
            url = "https://studio.youtube.com/youtubei/v1/video_manager/metadata_update?alt=json&key={}".format(self.ytb_info.INNERTUBE_API_KEY),
            headers = {
                "authorization": self.ytb_info.get_SAPISID_authorization(),
                "origin": "https://studio.youtube.com",
            },
            json = data)
        return res.status_code

    def uploadVideo(self, videoInfo):
        #step 1: Start a resumable session -> need "frontendUploadId" -> get upload_URI & scotty_resourceID
        #step 2: Create Video ID -> need scotty_resourceID, title, privacy, isdraft ->get videoID
        #step 3: Upload video uploadURI -> need videopath, uploadURI -> get status upload
        #step 3: Update video metadata -> need video InfoMation -> get status update
        upload_URI, scotty_resourceID = self.step_1_make_session(videoInfo["videoPath"])
        videoId = self.step_2_create_video_ids(scotty_resourceID, title= videoInfo["title"].replace(" ", "_"))
        
        print(videoId)
        videoInfo.update({
            "videoId": videoId
        })

        status_code = self.step_3_upload_video(upload_URI, videoInfo["videoPath"])
        status_code = self.step_4_update_video_infomation(videoInfo)
        return status_code