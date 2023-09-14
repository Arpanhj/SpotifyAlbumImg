import json,requests
TOKEN = "BQDS8KKVG1GXtrZDmFu_vatFupiLybhdpIs1dBrnd8FjPHV0HtROnVV3ziZlb0CLnoFKmD3xlXLDKQeFWM87JEWxQdb4wTVL4QbgOGWBRyhqzlgOfwo"

def createToken():
	gettoken1 = requests.post(url="https://accounts.spotify.com/api/token", headers={"Content-Type":"application/x-www-form-urlencoded"}, data="grant_type=client_credentials&client_id=83f4924033cd4ea1a5869475869d2638&client_secret=7d4b0bbcd781447ba4fd5604648385ff").json()
	
	return gettoken1['access_token']
def makeRequest(token, link):
	madeurl = f"https://api.spotify.com/v1/albums/{link}"
	json = requests.get(url=madeurl, headers={"Authorization":f"Bearer {token}"}).json()
	return json

#print("yay 1")
#rawdata = makeRequest(TOKEN, "78bpIziExqiI9qztvNFlQu").json()
#print("yay 2")
#print(rawdata)
#file = open("jsondump.txt","w")
#file.write(str(rawdata))
#file.close()

def getImgStuff(rawin):
	list = rawin['images']
	for i in list:
		print(f"{i['height']}x{i['width']} {i['url']}")
def linkToID(txt):
	return txt.split("/")[4].split("?")[0]

LINK = linkToID(input("input album link: "))
TOKEN = createToken()
raw = makeRequest(TOKEN,LINK)
getImgStuff(raw)

