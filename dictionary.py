import json
from difflib import get_close_matches
data=json.load(open("data.json"))
c=1
while c !=0 :
    wrd=input("ENTER THE WORD :  ")
    wrd=wrd.lower()
    if wrd in data:
        print(data[wrd])
    elif len(get_close_matches(wrd,data.keys()))>0:
        ai=input("Did You Mean %s insted ? Enter Y for YES & N for NO: "%get_close_matches(wrd,data.keys())[0])
        if ai=="Y" or ai=="y":
            print(data[get_close_matches(wrd,data.keys())[0]])
        else:
            print("Didn't Understand .PLEASE RETRY")
    else:
        print("WORD NOT EXIST!!")
    c=int(input("ENTER 1 TO SEARCH AGAIN & 0 TO EXIT : "))
