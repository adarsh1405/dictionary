import json
data=json.load(open("data.json"))
c=1
while c !=0 :
    wrd=input("ENTER THE WORD :")
    wrd=wrd.lower()
    if wrd in data:
        print(data[wrd])
    else:
        print("WORD NOT EXIST!!")
    c=int(input("ENTER 1 TO SEARCH AGAIN & 0 TO EXIT : "))
