
from turtle import *
from random import randint

# --- Ruut taustaks ---
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

# --- Abifunktsioon teksti näitamiseks ruudu sees ---
def kiri(sõnum, y_offset=0):
    goto(-side/2 + 20, side/2 - 60 + y_offset)
    write(sõnum, font=("Courier", 14, "normal"))

# --- Pangaautomaat ---
kood1 = "1234"
kood2 = "0000"

# Kuvame algteate ruudu sees
kiri("Tere tulemast pangaautomaati!")

# Küsi PIN-id (turtle akna kaudu, ruut jääb alles)
pin1 = textinput("PIN-sisestus", "Palun sisesta PIN-1:")
pin2 = textinput("PIN-sisestus", "Palun Sisesta PIN-2:")

# Kontrollime PIN-e
if kood1 == pin1 and kood2 == pin2:
    konto = 100
    kiri("Sisenesite kontosse!\n", -50)
    kiri("Teie kontol on " + str(konto) + " €.", -60)
    
    soovitud_raha = textinput("Väljavõtt", "Palju soovite välja võtta?")
    try:
        soovitud_raha = int(soovitud_raha)
    except:
        kiri("Vale sisestus!", -90)
        exitonclick()

    if soovitud_raha <= konto:
        konto -= soovitud_raha
        kiri(f"Võtsite {soovitud_raha} € välja!", -120)
        kiri(f"Alles on {konto} €.", -150)
    else:
        kiri("Kontol on liiga vähe raha!", -120)
        casino = textinput("Kasiino", "Kas soovite teenida raha juurde? (jah/ei)")
        if casino and casino.lower() == "jah":
            kasutaja_valik = textinput("Kasiino", "Red (1) või Black (2)?")
            try:
                kasutaja_valik = int(kasutaja_valik)
            except:
                kiri("Vale sisestus!", -150)
                exitonclick()
            suvaline_arv = randint(1, 2)
            if kasutaja_valik == suvaline_arv:
                konto += 100
                kiri(f"BIG WIN! Te võitsid Paksu Rihardi ja 100€!", -150)
                kiri(f"Teie kontol on nüüd {konto}€ ja Paks Rihard.", -180)
            else:
                konto = 0
                kiri("Sa kaotasid kogu oma raha :(", -150)
        else:
            kiri("Ole vaene rott edasi siis...", -150)
else:
    kiri("Vale PIN! Konto on lukustatud!", -30)

exitonclick()