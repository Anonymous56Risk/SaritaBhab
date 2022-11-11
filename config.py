#

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "29399732")
        self.API_HASH: str = os.environ.get("API_HASH", "11aea6465aa3ddf4bb831a5cc0b825f5")
        self.SESSION: str = os.environ.get("SESSION", "AQC6fEM8nPEA1GKmo_NnbxqwIA032g3W9uJGuS8zI9IqZCNLfzrx9XDPwDqbGsnlnNsOLIiiYMXZ3b2E8MQNIstN2puexNm8LeQSP64sf-w9vgZfQsia--2qv4iK9HsD9GX7mMe3T5y4BmNr3gST9gaa0j08P0pw8iANerlfLBOhzEyuCfIBk9Nw0OFc2OWjZ_I9u5JjLB-B3GxSS1QYqe2huZIAVXOnnJtZ8Ta7dmS8TUzIWlyQM-7LUH1VjVRigcAO5hU_Cj-XNRgvziRZDJwyfyyjErDyWe24BiqPkrw7TgIIe9GZLPht5C7yGAP4xiCUHRfaqk1SmqWcJFeHGs0YAAAAAVXgRhQA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5404761904").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
