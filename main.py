from insta_reel_liker import InstaLikes
import time

# enter your username or email and password inside the quotes below
USERNAME = ''
PASSWORD = ''

bot = InstaLikes()
bot.login(USERNAME, PASSWORD)
bot.load_reels()
for i in range(100):
    bot.like_reels()
    time.sleep(10)
print('done')