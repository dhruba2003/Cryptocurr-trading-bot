import requests
import time
import timeit
from plyer import notification
from datetime import datetime


i=0
j=0
A=["btcinr","xrpinr","ethinr","trxinr","eosinr","zilinr","batinr","zrxinr","omginr","polyinr","iostinr","dentinr","hotinr","usdtinr","wrxinr","maticinr","bchinr","bnbinr","bttinr","chzinr","oneinr","yfiinr","uniinr","linkinr","sxpinr","adainr","nanoinr","atominr","xlminr","fetinr","xeminr","zecinr","busdinr","yfiiinr","dogeinr","dotinr","vetinr","crvinr","reninr","enjinr","manainr","hbarinr","umainr","chrinr","paxginr","1inchinr","etcinr","uftinr","dockinr","filinr","wininr","tkoinr","pushinr","avaxinr","lunainr","xvginr","scinr","fttinr","dgbinr","cvcinr","cakeinr","ezinr","bzrxinr","ftminr","hntinr","arkinr","ctsiinr","kmdinr","solinr","cotiinr","iotxinr","shibinr","rlcinr","trbinr","reefinr","icpinr","ontinr","ckbinr","pntinr","xvsinr","viteinr","dcrinr","mdxinr","phainr","runeinr","ogninr","mirinr","datainr","ksminr","nkninr","balinr","dntinr","keepinr","snxinr","axsinr","celrinr","alphainr","compinr","aliceinr","egldinr","klayinr","sandinr","frontinr","ltcinr","dashinr"]
while True:
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
#NOTIFIER
    def a(t,me):
        if __name__ == "__main__":
            notification.notify(
                title=t,
                message=me,

                # displaying time
                timeout=2
        )
#__________________________________________________________________________________________________________________________________________________________________________________________________________________
#Initiation
    res = requests.get('https://api.wazirx.com/api/v2/tickers')
    #print(res.status_code)
    f=res.json()
    if (j%3==0):
        three = requests.get('https://api.wazirx.com/api/v2/tickers')
        threee = three.json()
    if(j%5==0):
        five = requests.get('https://api.wazirx.com/api/v2/tickers')
        fivee = five.json()
    if(j%10==0):
        ten = requests.get('https://api.wazirx.com/api/v2/tickers')
        tene = ten.json()

    time.sleep(1)
    re = requests.get('https://api.wazirx.com/api/v2/tickers')
    t = re.json()


#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    intimin=now.strftime("%M")
    print(intimin)
    print("Current Time =", current_time)
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#DATA MANIPULATION
    print(re.status_code)
    for r in range(0,len(A)-1):
        if float(t[A[r]]['last'])!=0:
            p = ((float(t[A[r]]['last']) - float(f[A[r]]['last'])) / float(f[A[r]]['last'])) * 100
            if p > 1.5:
                a(A[r], "PUMPING UP, price up by " + str(p) + " %")

    for ry in range(0, len(A) - 1):
       if float(t[A[ry]]['last']) != 0:
           if float(t[A[ry]]['last']) < float(f[A[ry]]['last']) :
             ee = (-(float(t[A[ry]]['last']) +float(f[A[ry]]['last'])) / float(f[A[ry]]['last'])) * 100
             if ee > 3:
                  a(A[ry], "GOING DOWN, price up by -" + str(ee) + " %")
    if()
    if (i % 3 == 0):
        threeee = requests.get('https://api.wazirx.com/api/v2/tickers')
        for rk in range(0, len(A) - 1):
            if float(threeee[A[rk]]['last']) != 0:
                qwe = ((float(threeee[A[rk]]['last']) - float(threee[A[rk]]['last'])) / float(threeee[A[rk]]['last'])) * 100
                if qwe > 1.5:
                    a(A[rk], "PUMPING UP, price up by " + str(qwe) + " % in 3 minutes")
    if (i % 5 == 0):
        fif = requests.get('https://api.wazirx.com/api/v2/tickers')
        for rkk in range(0, len(A) - 1):
            if float(t[A[rkk]]['last']) != 0:
                vdf = ((float(fif[A[rkk]]['last']) - float(fivee[A[rkk]]['last'])) / float(fif[A[rkk]]['last'])) * 100
                if vdf > 1.5:
                    a(A[rkk], "PUMPING UP, price up by " + str(vdf) + " % in 5 minutes")
    if (i % 10 == 0):
        tenn = requests.get('https://api.wazirx.com/api/v2/tickers')
        for rku in range(0, len(A) - 1):
            if float(t[A[rku]]['last']) != 0:
                ger = ((float(tenn[A[rku]]['last']) - float(tene[A[rku]]['last'])) / float(tenn[A[rku]]['last'])) * 100
                if ger > 1.5:
                    a(A[rku], "PUMPING UP, price up by " + str(ger) + " % in 10 minutes")


    #mdx=float(t['mdxinr']['last'])
    #if mdx <150:
        #   a('mdx', "PUMPING down, price up by ")
    #a('front :',str(t['frontinr']['last']))

    #SPECIAL TEMLATES FOR UNIQUES
    # s=((float(t['hntinr']['last'])-float(t['hntinr']['last']))/float(t['hntinr']['last']))*100
     # if s<-2:
    #    a("hntinr","GOING DOWN by :"+str(s)+" %")

    # k = ((float(t['alphainr']['last']) - float(t['alphainr']['last'])) / float(t['alphainr']['last'])) * 100
    #if k<-1.5:
      #  a("mirinr", "GOING DOWN by :" + str(k) + " %")
    i=i+1
    j=j+1
    print("running")







