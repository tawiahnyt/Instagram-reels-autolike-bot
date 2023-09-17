from insta_reel_liker import InstaLikes
import time

# enter your username or email and password inside the quotes below
USERNAME = ''
PASSWORD = ''

# Login to Instagram
bot = InstaLikes()
bot.login(USERNAME, PASSWORD)
# Load reels
bot.load_reels()
# Like reels
for i in range(100):
    bot.like_reels()
    time.sleep(10)
print('done')