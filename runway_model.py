import subprocess
import requests

url = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz'
r = requests.get(url, allow_redirects=True)

open('ngrok-stable-linux-amd64.tgz', 'wb').write(r.content)

subprocess.call("ls && ./ngrok authtoken 1siBHweElRgvcNTEIHUR49WPfcv_5rbwdTbBB5q9cMLJwYcme && ./ngrok tcp 22 --log=stdout > ngrok.log", shell=True)
subprocess.call("cat ngrok.log && ps -x && ls", shell=True)
