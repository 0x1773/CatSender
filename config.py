import json, os
from os import system
system('clear')
token = input("\033[1;37;45mAccess Token\033[1;37;40m ")
config = {
	"token": token
}
conf = json.dumps(config)
with open("config.json", "w") as f:
	f.write(conf)
	print("\033[1;37;42msuccess\033[1;37;40m Successfully wrote token to config.json")
	print("\033[1;37;41mExiting\033[1;37;40m")
	exit()
