print("Hello You!, ik ben Scott")
print("Wie ben jij?")
name = input("type hier je naam:")
print("Hello " + name)
print("Ik ben een nieuwkomer op het Mediacollege en ik ga daar over wat vragen stellen")

print("In welke stad ging ik eerst naar school?")
print("A: Hoorn")
print("B: Purmerend")
print("C: Amsterdam")
Antwoord_1 = input("Type hier je antwoord>")

if Antwoord_1 == "A" :
	print("Dat is fout!, het was Purmerend.")
elif Antwoord_1 == "B" :
	print("Dat klopt!")
elif Antwoord_1 == "C" :
	print("Dat is fout!, het was Purmerend.")


print("volgende vraag:")
print("Welke talen spreek ik?")
print("A: Nederlands en Engels")
print("B: Nederlands en Italiaans")
print("C: Nederlands en Duits")
Antwoord_2 = input("Type hier je antwoord!")

if Antwoord_2 == "A" :
	print("Dat klopt!")
elif Antwoord_2 == "B" :
	print("Nee! ik spreek geen Italiaans, maar wel engels!")
elif Antwoord_2 == "C" :
	print("Nee! ik spreek maar een heel klein beetje Duits, maar wel engels!")

print("Er komt nog 1 vraag aan")
print("hoe vond je het tot nu toe?")
Middel_vraag = input()

print("oke")
print("De laatste vraag:")
print("Welke richting wil ik op?")
print("A: Media developer")
print("B: Game developer")
print("C: Weet ik nog niet")
route_1 = False
Antwoord_3 = input("Type hier je antwoord>")
if Antwoord_3 == "A" :
	print("Fout! Ik weet het nog niet")
	
elif Antwoord_3 == "B" :
	print("Fout! ik weet het nog niet")
	
elif Antwoord_3 == "C" :
	print("Dat klopt!")
	route_1 = True

if route_1 == True:
        print("Omdat je de vorige vraag goed had krijg je deze bonus vraag!")
        print("Aan welke sport doe ik?")
        print("A: voetbal")
        print("B: Basketbal")
        print("C: tennis")
        antwoord_route_1 = input("Type hier je antwoord>")
        if antwoord_route_1 == "A":
                print("Dat is fout! Het is basketbal!")
        elif antwoord_route_1 == "B":
                print("Dat is goed! Ik zit inderdaad op basketbal!")
        elif antwoord_route_1 == "C":
                print("Dat is fout! Het is basketbal!")
else:
        print("Wat jammer dat je de vorige vraag fout had, anders had je een bonus vraag gekregen")
        
print("dit was de quiz")

