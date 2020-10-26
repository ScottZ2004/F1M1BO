# Dit zijn de variabelen!
import os
os.system("cls")
inleiding = False
stukje_1 = False
stukje_2 = False
stukje_3 = False
stukje_4 = False
stukje_5 = False
stukje_6 = False
stukje_7 = False
stukje_8 = False
stukje_9 = False
stukje_10 = False
stukje_11 = False
stukje_12 = False
stukje_13 = False
stukje_14 = False
stukje_15 = False
stukje_16 = False
stukje_17 = False
stukje_18 = False
stukje_19 = False
stukje_20 = False
stukje_21 = False
stukje_22 = False
stukje_23 = False
stukje_24 = False
stukje_25 = False
stukje_26 = False
stukje_27 = False
stukje_28 = False
stukje_29 = False
stukje_30 = False
einde_1 = False
einde_2 = False
einde_3 = False
einde_4 = False
einde_5 = False
einde_6 = False
spellteje = False
#-------------------------------------------------------------------------------

#introductie
print("Welkom bij het keuzeverhaal van Amir.")
print("Je krijgt zodirect stukjes tekst te zien die het verhaal van Amir vertellen.")
print("Daarna krijg je twee keuzes, A of B. De keuzes die jij maakt hebben invloed op het vrehaal.")
print("Laten we beginnen!")
print("(druk op enter om verder te gaan)")
Druk_op_enter_1 = input(">>>")
print("")

inleiding = True
spelletje = True
#inleiding
#---------------------------------------------------------------------------------
while spelletje == True:
    
    while inleiding == True:
        print("Inleiding,")
        print("")
        print("Stel je voor; je naam is Amir, je bent een jongen van 17 jaar en je woont met je moeder en je twee zusjes in de Syrische stad Aleppo.")
        print("Er is al negen jaar een burgeroorlog in het land en je vader zit in het leger om tegen ISIS te vechten, daardoor moet jij voor het gezin zorgen.")
        print("(druk op enter om verder te gaan)")
        Druk_op_enter_1 = input(">>>")
        print("")
        stukje_1 = True
        inleiding = False
    

#Stukje_1
    while stukje_1 == True:
        print("Voor het vertrek")
        print("")
        print("Je wordt wakker op een vroege donderdagochtend.")
        print("Je hebt goed geslapen, maar de dag zou heel anders lopen dan dat je had verwacht.")
        print("Om 14:00 uur hoor je een zwaar brommend geluid.")
        print("Het brommen wordt harder en harder te worden.")
        print("Toen je naar buiten liep zag je een vloot met vliegtuigen.")
        print("Je rent terug naar binnen en je gaat met je familie richting de kelder daar is het veilig. ")
        print("Een paar seconden later hoor je de bommen ontploffen en huizen die kapotgingen, ook hoor je mensen gillen en schreeuwen.")
        print("Na vijf minuten is het bombardement over en dan loop je naar buiten om te kijken wat de schade is.")
        print("Je ziet dat jouw huis deels weggeblazen is maar andere families zijn er erger aan toe.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat andere mensen helpen.")
        print("  B. Je gaat met je familie een plan maken om te vluchten.")
        Antwoord_1 = input(">>>")
    
        if Antwoord_1 == "A":
            stukje_2 = True
            stukje_1 = False
        
        elif Antwoord_1 == "B":
            stukje_6 = True
            stukje_1 = False

        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_2
    while stukje_2 == True:
        print("Je gaat richting je buurman om te kijken hoe het met hem gaat.")
        print("Als je bij zijn huis aankomt zie je dat hij vastzit onder het puin.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat hem proberen uit het puin te bevrijden.")
        print("  B. Je gaat aan andere vragen om je te helpen.")
        Antwoord_2 = input(">>>")
        if Antwoord_2 == "A":
            stukje_4 = True
            stukje_2 = False
        
        elif Antwoord_2 == "B":
            stukje_3 = True
            stukje_2 = False

        else:
            
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_3
    while stukje_3 == True:
        print("Je rent naar een andere man en je vraagt hem om je te helpen. ")
        print("Helaas komen jullie te laat.")
        print("Je buurman is al overleden doordat er een deel van de muur op zijn borstkas is geplet.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat terug richting je familie.")
        print("  B. Je gaat verder helpen.")
        Antwoord_3 = input(">>>")
        if Antwoord_3 == "A":
            stukje_6 = True
            stukje_3 = False
        elif Antwoord_3 == "B":
            stukje_5 = True
            stukje_3 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_4
    while stukje_4 == True:
        print("Je buurman ligt onder het puin, je haalt brokken steen en ander puin van hem vandaan en dan bevrijd je hem. ")
        print("Een paar seconden later stort er nog een groter deel van het huis in. Hij bedankt je en dan ga je weer verder.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat terug richting je familie.")
        print("  B. Je gaat verder helpen.")
        Antwoord_4 = input(">>>")
        if Antwoord_4 == "A":
            stukje_8 = True
            stukje_4 = False
        elif Antwoord_4 == "B":
            stukje_7 = True
            stukje_4 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_5
    while stukje_5 == True:
        print("Nadat je verder hebt geholpen ga je weer terug naar je familie.")
        stukje_6 = True
        stukje_5 = False

#stukje_6
    while stukje_6 == True:
        print("Je bent bij je familie en je besluit om te gaan vluchten, maar je hebt nog geen idee hoe.")
        print("Dan kom je met het idee om naar Turkije te gaan om te kijken of je daar kan worden opgevangen door hulpverleners.")
        print("Helaas is jullie auto door het bombardement gesloopt, dus de auto is geen optie.")
        print("")
        print("Hoe ga je naar Turkije?")
        print("")
        print("  A. Je gaat met de bus naar de grens.")
        print("  B. Je gaat te voet naar de grens")
        Antwoord_6 = input(">>>")
        if Antwoord_6 == "A":
            stukje_10 = True
            stukje_6 = False
        elif Antwoord_6 == "B":
            stukje_9 = True
            stukje_6 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
# Stukje_7
    while stukje_7 == True:
        print("Nadat je verder hebt geholpen ga je weer terug naar je familie.")
        stukje_8 = True
        stukje_7 = False

# Stukje_8
    while stukje_8 == True:
        print("Je bent bij je familie en je besluit om te gaan vluchten, maar je hebt nog geen idee hoe.")
        print("Ineens komt je buurman binnen, ")
        print("hij heeft een vriend die jullie kan smokkelen naar Turkije,")
        print("maar jullie kunnen niet tegelijk gesmokkeld worden.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je kiest ervoor om jezelf eerst te laten smokkelen en daarna je moeder en zusjes")
        print("  B. Je kiest er niet voor om gesmokkeld te worden en jullie gaan te voet naar de grens")
        Antwoord_8 = input(">>>")
        if Antwoord_8 == "A":
            stukje_13 = True
            stukje_8 = False
        elif Antwoord_8 == "B":
            stukje_9 = True
            stukje_8 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
#--------------------------------------------------------
# De Reis
    print("De Reis")
    print("")
# Stukje_9
    while stukje_9 == True:
        print("Jij en je familie gaan te voet richting de grens. ")
        print("Als jullie 13 uur later aankomen bij de grens laat de grensbewaking jullie er niet door omdat jij geen paspoort hebt.")
        print("Je vraagt of je hem iets kan geven om jullie over de grens te laten gaan.")
        print("Hij twijfelt even maar daarna vraagt hij om tienduizend lira.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je geeft hem het geld.")
        print("  B. Je geeft hem het geld niet.")
        Antwoord_9 = input(">>>")
        if Antwoord_9 == "A":
            stukje_11 = True
            stukje_9 = False
        elif Antwoord_9 == "B":
            stukje_12 = True
            stukje_9 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_10
    while stukje_10 == True:
        print("Je loopt met je familie naar het busstation om de bus richting de grens te pakken.")
        print("Na een uur in de bus te zitten komen jullie aan bij de grens.")
        print("Als je bij de grensbewaking aankomt weigert hij jullie er door te laten omdat jij geen paspoort bij je hebt. ")
        print("Je vraagt of je hem iets kan geven om jullie er door te laten. ")
        print("Hij twijfelt even maar daarna vraagt hij om tienduizend lira.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je geeft hem het geld.")
        print("  B. Je geeft hem het geld niet.")
        Antwoord_10 = input(">>>")
        if Antwoord_10 == "A":
            stukje_11 = True
            stukje_10 = False
        elif Antwoord_10 == "B":
            stukje_12 = True
            stukje_10 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
# stukje_11
    while stukje_11 == True:
        print("Je geeft het geld aan de grenswachter en dan laat hij jullie de grens over. ")
        print("Jullie worden een paar honderd meter over de grens opgevangen door hulpverleners.")
        print("Die hulpverleners brengen jullie naar een kamp waar jullie veilig zijn. ")
        print("")
        einde_1 = True
        stukje_11 = False

#stukje_12
    while stukje_12 == True:
        print("Je geeft het geld niet maar jouw moeder en zusjes gaan wel de grens over.")
        print("Jij gaat op een andere manier proberen een vluchtelingenkamp te bereiken. ")
        print("Dan kom je iemand tegen die je de grens over kan smokkelen.")
        print("Hij vraagt om vijftienduizend lira.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je geeft die smokkelaar vijftienduizend lira en je gaat met hem de grens over.")
        print("  B. Je weigert de smokkelaar en je vraagt nog een keer anan de grens wachter om je er door te laten")
        Antwoord_12 = input(">>>")
        if Antwoord_12 == "A":
            stukje_16 = True
            stukje_12 = False
        elif Antwoord_12 == "B":
            stukje_15 = True
            stukje_12 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
#stukje_13
    
    while stukje_13 == True:
        print("De volgende dag ontmoet je de smokkelaar.")
        print("Normaal zou je veel geld moeten betalen voor een smokkeling maar omdat jij je buurman hebt geholpen hoef jij maar tienduizend lira te betalen. ")
        print("De smokkelaar helpt je aan een illegaal paspoort en daarna gaan jullie meteen op pad. ")
        print("Als jullie bij de grens aankomen bekijkt de grenswachter jullie (illegale) paspoorten. ")
        print("Hij laat jullie uiteindelijk door en dan rijden jullie door richting het vliegveld. ")
        print("Als jullie aankomen vraagt hij of je op je gezin wilt wachten of dat je nu al het vliegtuig richting Athene neemt")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je wacht op je familie.")
        print("  B. Je gaat al meteen naar Athene")
        Antwoord_13 = input(">>>")
        if Antwoord_13 == "A":
            stukje_14 = True
            stukje_13 = False
        elif Antwoord_13 == "B":
            stukje_18 = True
            stukje_13 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#Stukje_14
    while stukje_14 == True:
        print("Je wacht een dag op het vliegveld en dan krijg je een belletje van je smokkelaar.")
        print("Hij zegt dat je moeder en zusjes zijn gepakt.")
        print("Op dit moment zitten ze in een vluchtelingenkamp vlak bij Kilis in Turkije.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat je familie opzoeken.")
        print("  B. Op het volgende vliegtuig richting Athene stappen en doorreizen (je familie is veilig in een kamp)")
        Antwoord_14 = input(">>>")
        if Antwoord_14 == "A":
            stukje_17 = True
            stukje_14 = False
        elif Antwoord_14 == "B":
            stukje_18 = True
            stukje_14 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

#stukje_15
    while stukje_15 == True:
        print("Je wijst het offer van de smokkelaar af. ")
        print("Je loopt weer naar de grenswachter en dan vraag je of je het geld alsnog kan betalen. ")
        print("Hij zegt ja en dan laat hij je de grens over.")
        print("Als je de grens over bent zoek je je familie en dan gaan jullie richting een vluchtelingenkamp. ")
        einde_1 = True
        stukje_15 = False

    #stukje_16
    while stukje_16 == True:
        print("Je geeft de smokkelaar het geld en dan brengt hij je de grens over. ")
        print("Dan komt hij met het voorstel om je naar het vliegveld te brengen en dan op een vliegtuig.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat naar je familie op zoek.")
        print("  B. Je gaat met het vliegtuig richting Athene.")
        Antwoord_16 = input(">>>")
        if Antwoord_16 == "A":
            stukje_17 = True
            stukje_16 = False
        elif Antwoord_16 == "B":
            stukje_18 = True
            stukje_16 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje_17
    while stukje_17 == True:
        print("Je gaat op zoek naar je familie. ")
        print("Na twee dagen zoeken kom je eindelijk aan bij het kamp waar je familie ook zit. ")
        einde_1 = True
        stukje_17 = False

    #stukje_18
    while stukje_18 == True:
        print("Je gaat met het vliegtuig richting Athene. ")
        print("Als je op het vliegveld staat krijg je te horen dat je familie ervoor heeft gekozen om naar een vluchtelingenkamp te gaan")
        print("Voordat je op het vliegtuig stapt word je nog even tegengehouden voor een paspoortcontrole. ")
        print("De controleur bekijkt je illegale paspoort ongeveer een seconde en dan laat hij je door. ")
        print("Na de vlucht kom je in Athene en dan word je opgevangen door een tweede smokkelaar.")
        print("Hij zegt dat je naar Engeland word gebracht. ")
        print("Na ongeveer twee weken verscholen in auto te zitten kom je aan in IJmuiden. ")
        print("Als jullie bij de haven zijn gaat je smokkelaar even weg om een ticket te kopen.")
        print("Hij heeft niets gezegd over waar hij heen gaat.")
        print("Dan zie je dat er een man richting de auto komt lopen.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je blijft zitten in de auto.")
        print("  B. Je gaat de auto uit.")
        Antwoord_18 = input(">>>")
        if Antwoord_18 == "A":
            stukje_19 = True
            stukje_18 = False
        elif Antwoord_18 == "B":
            stukje_20 = True
            stukje_18 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje_19
    while stukje_19 == True:
        print("Je blijft in de auto zitten.")
        print("Als die man de auto bereikt komt je smokkelaar net op tijd aan om zich te identificeren. ")
        print("Je bent erg opgelucht omdat je bijna was opgepakt")
        print("Als je eindelijk aankomt in Dover word je naar een asielzoekerscentrum gebracht en daar word je goed opgevangen. ")
        stukje_21 = True
        stukje_19 = False

    # stukje_20
    while stukje_20 == True:
        print("Je gaat de auto uit omdat je niet gepakt wilt worden. ")
        print("Nadat je de auto hebt verlaten sluip je de haven uit en ga je de menigte in. ")
        print("Na veel te vragen kom je aan in een asielzoekerscentrum. ")
        print("Je word goed opgevangen.")
        stukje_24 = True
        stukje_20 = False



    #stukje 21
    while stukje_21 == True:
        print("Je bent in een asielzoekerscentrum in Londen.")
        print("Bij je ondervraging word de vraag gesteld of je nog familie hebt.")
        print("")
        print("Wat zeg je?")
        print("")
        print("  A. Je zegt dat je nog familie hebt in Turkije.")
        print("  B. Je zegt dat je geen familie meer hebt.")
        Antwoord_21 = input(">>>")
        if Antwoord_21 == "A":
            stukje_22 = True
            stukje_21 = False
        elif Antwoord_21 == "B":
            stukje_23 = True
            stukje_21 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje 22
    while stukje_22 == True:
        print("Je zegt dat je nog familie hebt in een vluchtelingenkamp in Turkije. ")
        print("De medewerker van de immigratiedienst noteert dat en zegt dan dat je met hen verenigt kan worden als je een verblijfsvergunning krijgt.")
        print("Na twee maanden wachten krijg je eindelijk een verblijfsvergunning")
        stukje_27 = True
        stukje_22 = False

    #stukje 23
    while stukje_23 == True:
        print("je zegt dat je geen verdere familie hebt.")
        print("De medewerker van de immigratiedienst vraagt of je het zeker weet en dan zeg je dat ze niet meer leven.")
        print("Na twee maanden wachten krijg je eindelijk een verblijfsvergunning.")
        stukje_28 = True
        stukje_23 = False

    #stukje 24
    while stukje_24 == True:
        print("Je bent in een asielzoekerscentrum in Ter Apel. ")
        print("Bij je ondervraging word de vraag gesteld of je nog familie hebt.")
        print("")
        print("Wat zeg je")
        print("")
        print("  A. je zegt dat je nog familie hebt in Turkije")
        print("  B. Je zegt dat je geen familie meer hebt")
        Antwoord_24 = input(">>>")
        if Antwoord_24 == "A":
            stukje_25 = True
            stukje_24 = False
        elif Antwoord_24 == "B":
            stukje_26 = True
            stukje_24 = False
        
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje 25
    while stukje_25 == True:
        print("Je zegt dat je nog familie hebt in een vluchtelingenkamp in Turkije. ")
        print("De medewerker van de immigratiedienst noteert dat en zegt dan dat je met hen verenigt kan worden als je een verblijfsvergunning krijgt.")
        print("Na twee maanden wachten krijg je eindelijk een verblijfsvergunning.")
        stukje_29 = True
        stukje_25 = False

    #stukje 26
    while stukje_26 == True:
        print("Je zegt dat je geen verdere familie hebt. ")
        print("De medewerker van de immigratiedienst vraagt of je het zeker weet en dan zeg je dat ze niet meer leven.")
        print("Na twee maanden wachten krijg je eindelijk een verblijfsvergunning.")
        stukje_30 = True
        stukje_26 = False

    #stukje 27
    while stukje_27 == True:
        print("Een jaar later.")
        print("Je woont nu al een jaar in de wereldsad Londen. ")
        print("Je werkt in een restaurant vlak bij Piccadilly. ")
        print("Je hebt goed contact met je familie.")
        print("Omdat de oorlog net is afgelopen krijg je de keuze om terug naar je familie in Syrië te gaan. ")
        print("")
        print("Wat ga je doen")
        print("")
        print("  A. Je gaat terug naar je familie in Syrie")
        print("  B. Je blijft in londen")
        Antwoord_27 = input(">>>")
        if Antwoord_27 == "A":
            einde_2 = True
            stukje_27 = False
        elif Antwoord_27 == "B":
            einde_3 = True
            stukje_27 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
    # stukje 28
    while stukje_28 == True:
        print("Een maand later")
        print("Je woont  nu al een maand in Londen")
        print("Je werkt in een supermarkt en je hebt goed contact met je familie.")
        print("Je krijgt een bericht dat je familie kan worden ingevlogen omdat de oorlog is afgelopen.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je laat je familie invliegen")
        print("  B. Je gaat zelf terug naar Syrie")
        Antwoord_28 = input(">>>")
        if Antwoord_28 == "A":
            einde_4 = True
            stukje_28 = False
        elif Antwoord_28 == "B":
            einde_2 = True
            stukje_28 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje 29
    while stukje_29 == True:
        print("Een jaar later")
        print("Je woont nu al een jaar in Amsterdam.")
        print("Je werkt in een supermarkt en je hebt goed contact met je familie. ")
        print("Omdat de oorlog net is afgelopen krijg je de keuze om terug te gaan naar je familie in Syrië.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. Je gaat terug naar je familie in Syrie")
        print("  B. Je blijft in Amsterdam")
        Antwoord_29 = input(">>>")
        if Antwoord_29 == "A":
            einde_2 = True
            stukje_29 = False
        elif Antwoord_29 == "B":
            einde_5 = True
            stukje_29 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #stukje 30
    while stukje_30 == True:
        print("Een maand later")
        print("Je woont  nu al een maand in Amsterdam.")
        print("Je werkt in een supermarkt en je hebt goed contact met je familie. ")
        print("Je krijgt een bericht dat je familie kan worden ingevlogen omdat de oorlog is afgelopen.")
        print("")
        print("Wat ga je doen?")
        print("")
        print("  A. je laat je familie invliegen")
        print("  B. je gaat zelf terug naar Syrie")
        Antwoord_30 = input(">>>")
        if Antwoord_30 == "A":
            einde_6 = True
            stukje_30 = False
        elif Antwoord_30 == "B":
            einde_2 = True
            stukje_30 = False

        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    #einde1
    while einde_1 == True:
        print("Je spendeert een jaar in het kamp, totdat je het nieuws krijgt dat de burgeroorlog in Syrië is afgelopen.")
        print("Een week later word je terug naar Aleppo gestuurd.")
        print("Je hoopt dat er nooit meer zo iets vreselijks gebeurt.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E1 = input(">>>")
        if Antwoord_E1 == "A":
            inleiding = True
            einde_1 = False
        elif Antwoord_E1 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_1 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_2 == True:
        print("Je bent weer terug in Syrië met je familie.")
        print("Je woont in een nieuw huis in de stad Aleppo. ")
        print("Je hoopt dat er nooit meer zo iets vreselijks gebeurt.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E2 = input(">>>")
        if Antwoord_E2 == "A":
            inleiding = True
            einde_2 = False
        elif Antwoord_E2 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_2 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_3 == True:
        print("Je blijft in Londen wonen.")
        print("Je familie woont weer in Syrië en je bezoekt ze elk jaar in de zomer.")
        print("Je bent aan de studie politie agent begonnen in London.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E3 = input(">>>")
        if Antwoord_E3 == "A":
            inleiding = True
            einde_3 = False
        elif Antwoord_E3 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_3 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue
        
    while einde_4 == True:
        print("Je word herenigd met je familie")
        print("Jullie blijven in Engeland wonen omdat jullie het niet meer vertrouwen in Syrië.")
        print("Je bent aan de studie politie agent begonnen in Londen.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E4 = input(">>>")
        if Antwoord_E4 == "A":
            inleiding = True
            einde_4 = False
        elif Antwoord_E4 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_4 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_5 == True:
        print("Je blijft in Amsterdam wonen.")
        print("Je familie woont weer in Syrië en je bezoekt ze elk jaar in de zomer")
        print("Je bent aan de studie verpleegkundige begonnen in Zaandam.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E5 = input(">>>")
        if Antwoord_E5 == "A":
            inleiding = True
            einde_5 = False
        elif Antwoord_E5 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_5 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    while einde_6 == True:
        print("Je word herenigd met je familie.")
        print("Jullie blijven in Nederland wonen omdat jullie het niet meer vertrouwen in Syrië")
        print("Je bent aan de studie verpleegkundige begonnen in Zaandam.")
        print("")
        print("Dit was het einde van dit spelletje.")
        print("wil je nog een keer spelen?")
        print("")
        print("  A. Ja! ik wil graag nog een keer spelen!")
        print("  B. Nee. ik hoef niet nog een keer te spelen.")
        Antwoord_E6 = input(">>>")
        if Antwoord_E6 == "A":
            inleiding = True
            einde_6 = False
        elif Antwoord_E6 == "B":
            print("Bedankt dat je dit spel hebt gespeeld!")
            print("Tot ziens!")
            spelletje = False
            einde_6 = False
        else:
            print("Je moet wel goed antwoorden! Let goed op de hoofdletter")
            print("")
            continue

    
