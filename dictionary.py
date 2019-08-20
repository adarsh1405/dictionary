import json
data=json.load(open("data.json"))
wrd=input("ENTER THE WORD :")

if wrd in data:
    print(data[wrd])
else:
    print("WORD NOT EXIST!!")
