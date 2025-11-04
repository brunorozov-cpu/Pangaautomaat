from turtle import *
from random import randint

# Ruut taust
side = 600
penup()
goto(-side/2, -side/2)
pendown()
color("black", "orange")
begin_fill()
for i in range(4):
    forward(side)
    left(90)
end_fill()
penup()
hideturtle()

def kiri(sõnum, y_offset=0):
    goto(-side/2 + 20, side/2 - 60 + y_offset)
    write(sõnum, font=("Courier", 14, "normal"))

# Vale PIN code
teade = Turtle()
teade.hideturtle()
teade.penup()
teade.goto(-side/2 + 20, side/2 - 90)
teade.color("black")

# Pangaautomaat
kood1 = "1234"
kood2 = "0000"

kiri("Tere tulemast pangaautomaati!")

# PIN-kontroll 3 katsega
katseid = 3
while katseid > 0:
    pin1 = textinput("PIN-sisestus", "Palun sisesta PIN-1:")
    pin2 = textinput("PIN-sisestus", "Palun sisesta PIN-2:")
    
    if kood1 == pin1 and kood2 == pin2:
        teade.clear()
        break
    else:
        katseid -= 1
        teade.clear()  # <<<Kustutab eelmise teate
        if katseid > 0:
            teade.write(f"Vale PIN! Jäänud on {katseid} katset.", font=("Courier", 14, "normal"))
        else:
            teade.write("Konto on lukustatud!", font=("Courier", 14, "normal"))
            exitonclick()

# Kui PIN õige
konto = 100
kiri("Sisenesite kontosse!\n", -80)
kiri("Teie kontol on " + str(konto) + " €.", -100)

soovitud_raha = textinput("Väljavõtt", "Palju soovite välja võtta?")
try:
    soovitud_raha = int(soovitud_raha)
except:
    kiri("Vale sisestus!", -130)
    exitonclick()

if soovitud_raha <= konto:
    konto -= soovitud_raha
    kiri(f"Võtsite {soovitud_raha} € välja!", -160)
    kiri(f"Alles on {konto} €.", -190)
else:
    kiri("Kontol on liiga vähe raha!", -160)
    casino = textinput("Kasiino", "Kas soovite teenida raha juurde? (jah/ei)")
    if casino and casino.lower() == "jah":
        kasutaja_valik = textinput("Kasiino", "Red (1) või Black (2)?")
        try:
            kasutaja_valik = int(kasutaja_valik)
        except:
            kiri("Vale sisestus!", -190)
            exitonclick()
        suvaline_arv = randint(1, 2)
        if kasutaja_valik == suvaline_arv:
            konto += 100
            kiri(f"BIG WIN! Te võitsid Paksu Rihardi ja 100€!", -190)
            kiri(f"Teie kontol on nüüd {konto}€ ja Paks Rihard.", -220)
        else:
            konto = 0
            kiri("Sa kaotasid kogu oma raha :(", -190)
    else:
        kiri("Ole vaene rott edasi siis...", -190)

exitonclick()
