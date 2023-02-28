# to be able to use secrets.py
import os
# append 03_misc with secrets.py to path
cwd = os.getcwd()
misc_pack_path = os.path.join(cwd, r"../03_misc/")
import sys
sys.path.append(r"C:\Users\tvsii\Desktop\Repositories\hivemind\03_misc")

from api_secrets import bearer_token

print("All went well.")
print(bearer_token)