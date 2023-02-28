# to be able to use secrets.py
import os
# append 03_misc with secrets.py to path
cwd = os.getcwd()
misc_pack_path = os.path.join(cwd, r"../03_misc/")
import sys
sys.path.append(r"C:\Users\tvsii\Desktop\Repositories\hivemind\03_misc")

import api_secrets as s
import tweepy

# OAuth process, using the keys and tokens
auth = tweepy.OAuth1UserHandler(
   s.api_key, s.api_key_secret, s.access_token, s.access_token_secret
)

auth.set_access_token(s.access_token, s.access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# lebran jams
userID = "KingJames"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")





