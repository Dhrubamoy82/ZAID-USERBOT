import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome To Zaid Userbot'

os.system("python3 -m Zaid")
if __name__ == "__main__":
    app.run()
