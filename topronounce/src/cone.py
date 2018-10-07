import  configparser
from pathlib import Path
import os
df={ 1:'One', 2:'Two', 3:'Three'}

parser = configparser.ConfigParser()
dr=os.path.dirname(os.path.abspath(__file__))
fdr=os.path.join(os.path.dirname(dr),"etc/simple.ini")
parser.read(fdr)


def conver(x):
    return df[x]+parser.get('bug', 'url')

def ty():
    parser = configparser.ConfigParser()
    parser.read("simple.ini")
    return parser.get('bug', 'url')

