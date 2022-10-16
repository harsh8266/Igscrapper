import requests,os
import argparse
import urllib.request
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="Enter User to Scan")
args = vars(ap.parse_args())
os.system("clear")
loginkey=input("Enter Key Generated From Rapid Api: ")
if args['user']:
	username=args["user"]
	print("Connectiong to Server:")
	url = f"https://instagram188.p.rapidapi.com/userid/{username}"
	headers = {"X-RapidAPI-Key": f"{loginkey}","X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	if a['success']==True:
		print("Connection Successful")
		userid=a['data']
	else:
		print("Connection Failed")

# To Download Profile picture
def profile_picture(username):
	url =f"https://instagram188.p.rapidapi.com/userphoto/{username}"
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	urllib.request.urlretrieve(a['data'],r'Output/profile_image.jpg')
	print("Image Saved in Output Folder")


print("Enter Commmands\nContact info : i\nProfile Photo : p\nQuit : q")
loop=True
while loop :
	command=input(">>")
	if command=="p":
		profile_picture(username)
	elif command=="i":
		pass
	elif command=="q":
		loop=False
	else:
		print("Invalid Command")

