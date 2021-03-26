import requests
from bs4 import BeautifulSoup
req=requests.get("http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding = "Big5"

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("p")
    fp=open("out2.txt","w",encoding="Big5")
    for val in result1:
        text2=val.text.replace('\n','')
        text3=text2.replace('  ','')
        text4=text3.replace('\xe9','')
        data=text4.split(",")
        for i in data:
            if '''“''' in i:
                print(i)
                fp.write(i+'\n')        
    fp.close()
else: 
    print("no page")