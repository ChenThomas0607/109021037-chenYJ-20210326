# 109021037-chenYJ-20210326
1.result1 = soup.find_all("p")
  原始碼含有p所以用p
2.text4=text3.replace('\xe9','')
3.        data=text4.split(",")
        for i in data:
            if '''“''' in i:
                print(i)
                fp.write(i+'\n')        
    fp.close()

