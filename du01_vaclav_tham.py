from turtle import circle, forward, left, pendown, penup, right, exitonclick, speed
#Program na hru piškvorky. Měl by splňovat funkčnost pro korektní vstupy, libovolná velikost pole.
#Strana ctverce
stranactverce=30
print("Ahoj právě si otevřel piškvorky")
print("Budeš vyzván, abys zadal velikost pole")

#zvolime si velikost hraciho pole
pocetsloupcu=int(input("Zadej počet sloupcu "))
#Ošetření chybných vstupů
while pocetsloupcu<1:
	pocetsloupcu=int(input("Zadal si chybnou hodnotu, zadej znovu počet sloupců "))
pocetradek=int(input("Zadej počet řádků "))
#Ošetření chybných vstupů
while pocetradek<1:
	pocetradek=int(input("Zadal si chybnou hodnotu, zadej znovu počet řádek "))

#Přiřazení počtu políček do proměnné
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
	
#Cyklus pro počet tahů
for f in range(nasobek):
#zadaní souřadnic
	radka= int(input("Zadej řádku "))
	#Ošetření chybných vstupů
	while (radka<1) or (radka>pocetradek):
		print("Zadal jsi špatnou řádku")
		radka= int(input("Zadej řádku "))
	sloupec= int(input("Zadej sloupec "))
	#Ošetření chybných vstupů
	while (sloupec<1) or (sloupec>pocetradek):
		print("Zadal jsi špatný sloupec")
		sloupec= int(input("Zadej sloupec "))
	
	#Ošetření zda je to lichý či sudý tah tj. zda má program kreslit křížek či kolečko
	if 	f%2==0:
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
	else:
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
print("Konec hry")
exitonclick()