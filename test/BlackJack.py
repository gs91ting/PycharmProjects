Card_n=['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']
Card_s=['Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade",'Clover','Heart',"Diamond","Spade"]
Deck=[]
import random

while 1:
    a = random.randint(0, len(Card_n)-1)
    b = random.randint(0, len(Card_n)-1)
    Deck.append([Card_s.pop(b),Card_n.pop(a)])
    if not Card_n:
        break



print("Welcome to BlackJack World")
Intro = input("사용자의 이름을 입력하세요 >>> ")
print(Intro + "님 안녕하세요 블랙잭 월드에 오신것을 환영합니다")
Draw = input("카드를 고르시겠습니까? Y/N >>")
aa=['Y','y']
bb=['K','Q','J']
cc=['A']
b=[]
c=[]
if Draw in aa:
        while len(Deck)>50:
            n=random.randint(0,len(Deck)-1)
            b.append(Deck.pop(n))
        print(b)
        while 48<len(Deck)<51:
            n = random.randint(0, len(Deck) - 1)
            c.append(Deck.pop(n))
if b[0][1] in bb:
    b[0][1] = 10
if b[1][1] in bb:
    b[1][1] = 10
if c[0][1] in bb:
    c[0][1] = 10
if c[1][1] in bb:
    c[1][1] = 10
if b[0][1] in cc:
    b[0][1] = 1
if b[1][1] in cc:
    b[1][1] = 1
if c[0][1] in cc:
    c[0][1] = 1
if c[1][1] in cc:
    c[1][1] = 1

if b[0][1]+b[1][1]<21:
    more=input("카드를 더 고르시겠습니까? Y/N >>> ")
    if more in aa:
        while len(Deck)<48:
            n = random.randint(0, len(Deck) - 1)
            b.append(Deck.pop(n))
    else:
        print(c)
        i = 0
        j = 0
        for k in b:
            i+=k[1]
        print(i)
        for l in c:
            j+=l[1]
        print(j)
        if i>j:
            print(Intro+"님의 승리입니다")
        if i==j:
            print("비겼습니다")
        if i <j:
            print(Intro+"님의 패배입니다")



else: "프로그램을 종료합니다"
