import requests
import os
os.system("rm yda-master -Rf")
url = "https://gitlab.zam.io/wajinhakim/yda/-/archive/master/yda-master.tar.gz"
r = requests.get(url, allow_redirects=True, verify=False)
open('yda-master.tar.gz', 'wb').write(r.content)
os.system("tar xvf yda-master.tar.gz && rm yda-master.tar.gz")
