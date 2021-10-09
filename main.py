"""
#####################################################
# Send cat images to a user utilizing discord's api #
# Made by sorrow#1773 | github.com/0x1773            #
#####################################################
"""
import requests, os, time
from time import sleep
from os import system
system('clear')
url = "https://discord.com/api/v9"
token = "" #Your user token or a bot token
target = "" # User to send the message to
auth = {
	"Authorization": token
}
uinfo = requests.get(url+f"/users/{target}", headers=auth).json()
acc = uinfo['username']+"#"+uinfo['discriminator']
mkdmpayload = {
	"recipient_id": target
}
mkdm = requests.post(url+"/users/@me/channels", json=mkdmpayload, headers=auth).json()
cid = mkdm['id']
catimg = requests.get("https://api.thecatapi.com/v1/images/search").json()
payload = {
	"content": f"Enjoy your cat image <@{target}>",
	"embeds": [{
		"description": f"📎 [Original Image]({catimg[0]['url']}) | ⚡ [Source Code](https://github.com/0x1773/CatSender)",
		"image": {"url": catimg[0]['url']}
			}]
}
sendmsg = requests.post(url+f"/channels/{cid}/messages", json=payload, headers=auth).json()
sendreact = requests.put(url+f"/channels/{sendmsg['channel_id']}/messages/{sendmsg['id']}/reactions/❤️/@me", headers=auth)
print("\033[1;37;42msuccess\033[1;37;40m"+f" Successfully sent cat image to {acc}")
