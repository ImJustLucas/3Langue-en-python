import platform
import cpuinfo
import socket
from flask import Flask, render_template

app = Flask(__name__)

class SystemInfo:
    def __init__(self):
        self.system = platform.system()
        self.processor = cpuinfo.get_cpu_info()['brand_raw']
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.memory = dict((i.split()[0].lower(), int(i.split()[1])) for i in open('/proc/meminfo').readlines())

@app.route('/')
def SPANISH(self):
    SystemInfoDeLaMuerte = SystemInfo()
    return render_template('index.html', system=self.system, processor=self.processor, hostname=self.hostname, ip_address=self.ip_address, memory=self.memory)
