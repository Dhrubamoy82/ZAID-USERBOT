import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5792746224").split()))
OWNER_ID = int(getenv("OWNER_ID", "5792746224"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Zaid:Zaid@cluster0.589z3sh.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5841845692:AAH0kjTW_o0OkC0b5sFz7I3Jy93REwUsD9Y")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkArdBwWiyJt3t9j25R0PZaj4YFzMtGaVcA4I2i-BIpKVk85YuM7ZCtN1is7uCTtUxeIW_A5OWdakVDNoV_dqPYprOtB1YwDg9osFMuVdwlDwAOWLJ5exo38sc9VjXCvGRwiOtE4FklRGVPr5gAQyub-UC4nkAEI16IPkBpJoDKUdb13MXdhtkcSRG-Llb815ni_2Vv5IojRnf5azFQwloX5mRmHCSATbtXp9-hBu83xbVpBn-jQTq0RJOV7LAc_8g8eMiK-YpJJnTimQCa6t10useFHz89zl4ql-4cFWIX366qm4O3doPUf9qoNBoTRlsAFMxkBBaQiaXC9qMM0JnE6wAAAAFZRkrwAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
