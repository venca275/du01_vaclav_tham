from turtle import circle, forward, left, pendown, penup, right, exitonclick, speed
#Program na hru piškvorky. Měl by splňovat funkčnost pro korektní vstupy, libovolná velikost pole.
#Strana ctverce
stranactverce=30
print("Ahoj právě si otevřel piškvorky")
hrac1= input("Zadej jmeno prvniho hrace: ")
hrac2= input("Zadej jmeno druheho hrace: ")
print ("V tomto duelu proti sobe nastoupí ", hrac1 ,"a ", hrac2 ,".")
#zvolime si velikost hraciho pole
pocetsloupcu=int(input("Zadej počet sloupcu "))
pocetradek=int(input("Zadej počet řádků "))
print("Tato hra piskvorek je v poli ",pocetsloupcu,"x",pocetradek)
nasobek=int(pocetsloupcu * pocetradek)
#Vykreslení hracího pole (síťe)
speed(0)
for _ in range(pocetradek):
	for _ in range(pocetsloupcu):
		for _ in range(4):
			forward(stranactverce)
			left(90)
		forward(stranactverce)
	left(180)
	forward(pocetsloupcu*stranactverce)
	right(90)
	forward(stranactverce)
	right(90)
#Ošetření počtu v lichý/sudý
if (nasobek%2==0):
	opakovani=int((nasobek)/2)
else:
	opakovani=int((nasobek-1)/2)	
for f in range(opakovani):
#zadaní souřadnic
	print(" Ted je na řadě hráč ",hrac2,)
	radka= int(input("Zadej řádku "))
	while (radka<1) or (radka>pocetradek):
		print("Zadal jsi špatnou řádku")
		radka= int(input("Zadej řádku "))
	sloupec= int(input("Zadej sloupec "))
	while (sloupec<1) or (sloupec>pocetradek):
		print("Zadal jsi špatný sloupec")
		sloupec= int(input("Zadej sloupec "))
	#Přesun na pozici
	penup()
	forward(sloupec * stranactverce - stranactverce)
	right(90)
	forward(radka * stranactverce - stranactverce)
	pendown()
	#Vykreslení křížku
	left(90)
	right(45)
	forward(4)
	pendown()
	forward(38)
	right(180)
	forward(19)
	right(90)
	forward(19)
	right(180)
	penup()
	forward(19)
	pendown()
	forward(19)
	right(180)
	penup()
	forward(19)
	left(90)
	forward(23)
	right(135)
	pendown()
	left(180)
	#Vrácení se na začátek
	penup()
	forward(sloupec * stranactverce - stranactverce)
	right(180)
	left(90)
	forward(radka * stranactverce - stranactverce)
	right(90)
	#zadání souřadnic
	print("Teď je na řadě hráč ",hrac1,)
	radka= int(input("Zadej řádku "))
	while (radka<1) or (radka>pocetradek):
		print("Zadal jsi špatnou řádku")
		radka= int(input("Zadej řádku "))
	sloupec= int(input("Zadej sloupec "))
	while (sloupec<1) or (sloupec>pocetradek):
		print("Zadal jsi špatný sloupec")
		sloupec= int(input("Zadej sloupec "))
	#Přesun na pozici
	penup()
	forward(sloupec * stranactverce - 26)
	right(90)
	forward(radka * stranactverce - 15)
	pendown()
	#Vykreslení kolečka
	circle(11)
	#Přesun zpět na začátek
	penup()
	right(90)
	forward(sloupec * stranactverce - 26)
	right(90)
	forward(radka * stranactverce - 15)
	right(90)
	pendown()
#Tah navic pokud je pocet policek lichy
if (nasobek%2==0):
	print("Konec hry")
else:
	print(" Ted je na řadě hráč ",hrac2,)
	radka= int(input("Zadej řádku "))
	while (radka<1) or (radka>pocetradek):
		print("Zadal jsi špatnou řádku")
		radka= int(input("Zadej řádku "))
	sloupec= int(input("Zadej sloupec "))
	while (sloupec<1) or (sloupec>pocetradek):
		print("Zadal jsi špatný sloupec")
		sloupec= int(input("Zadej sloupec "))
	#Přesun na pozici
	penup()
	forward(sloupec * stranactverce - stranactverce)
	right(90)
	forward(radka * stranactverce - stranactverce)
	#Vykreslení křížku
	left(90)
	right(45)
	forward(4)
	pendown()
	forward(38)
	right(180)
	forward(19)
	right(90)
	forward(19)
	right(180)
	penup()
	forward(19)
	pendown()
	forward(19)
	right(180)
	penup()
	forward(19)
	left(90)
	forward(23)
	right(135)
	pendown()
	left(180)
	#Vrácení se na začátek
	penup()
	forward(sloupec * stranactverce - stranactverce)
	right(180)
	left(90)
	forward(radka * stranactverce - stranactverce)
	right(90)
	print("Konec hry")
exitonclick()