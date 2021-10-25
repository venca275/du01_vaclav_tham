from turtle import circle, forward, left, pendown, penup, right, exitonclick
#Sloupce
x=3
#Radky
y=3
#Strana ctverce
a=30
print("Ahoj právě si otevřel piškvorky")
j= input("Zadej jmeno prvniho hrace: ")
k= input("Zadej jmeno druheho hrace: ")
print ("V tomto duelu proti sobe nastoupí ", j ,"a ", k ,".")
print("Tato hra piskvorek je v poli ",x,"x",y)
for _ in range(y):
	for _ in range(x):
		for _ in range(4):
			forward(a)
			left(90)
		forward(a)
	left(180)
	forward(x*a)
	right(90)
	forward(a)
	right(90)
print("Začíná hra jako první jde hráč ",j,)
radka= int(input("Zadej řádku "))
sloupec= int(input("Zadej sloupec "))
penup()
forward(sloupec * a - 26)
right(90)
forward(radka * a - 15)
pendown()
circle(11)
penup()
right(90)
forward(sloupec * a - 26)
right(90)
forward(radka * a - 15)
right(90)
pendown()
exitonclick()