import json
from requests import get
from json import dumps

def ipwhois(ip4:str) -> str:
    url = "https://ipwhois.app/json/%s"%(ip4);
    try:
        req = get(url).json()
        return json.dumps(req,indent=2,sort_keys=True)
    except:return "Check your internet connection!"

def main():
    while True:
        print("type quit/exit for exit the program\n")
        data = input("ip4 > ");
        if not data:
            print(ipwhois("0"));
        elif data in ["quit","exit"]:
            print("user quit :)");
            False;break;
        else:print(ipwhois(data));
