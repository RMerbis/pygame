# Importeer de benodigde modules: pygame voor grafische weergave, time voor pauzes, en random voor willekeurige waarden.
import pygame
import time
import random

# Initialiseer pygame om de functies te kunnen gebruiken.
pygame.init()

# Stel de breedte en hoogte van het scherm in.
breedte = 600
hoogte = 300

# Definieer de achtergrondkleur als wit (RGB-waarden).
background_color = 255, 255, 255

# Maak een venster met de opgegeven breedte en hoogte.
screen = pygame.display.set_mode((breedte, hoogte))

# Laad de afbeelding van de schildpad.
schildpad_origineel = pygame.image.load("schildpad.png")

# Kopieer de schildpad-afbeelding.
schildpad = pygame.image.load("schildpad.png")

# Maak de schildpad kleiner met behulp van transform.rotozoom (schalen met een factor van 0.5).
schildpad_origineel = pygame.transform.rotozoom(schildpad, 0, 0.5)

# Verkrijg een rechthoek rondom de schildpadafbeelding.
schildpad_rechthoek = schildpad.get_rect()

# Plaats de rechthoek (en dus de schildpad) in het midden van het scherm.
schildpad_rechthoek.center = (400, 150)

# Laad de afbeelding van een blaadje sla.
sla = pygame.image.load("sla.png")

# Verkrijg een rechthoek rondom de sla-afbeelding.
sla_rechthoek = sla.get_rect()

# Plaats de sla in het midden van het scherm op (100, 100).
sla_rechthoek.center = (100, 100)

# Stel de snelheid van de schildpad in als een lijst met x- en y-snelheid.
schildpad_snelheid = [1, 1] #aangepast om de schildpad schuin te laten lopen

# Variabele die aangeeft of de schildpad leeft.
dier_leeft = True

# Variabele om de honger van de schildpad bij te houden.
honger = 0

# Teller om bij te houden hoe vaak de sla van positie verandert.
spring_teller = 0

# Begin de hoofdloop van het spel. Deze loopt zolang de schildpad leeft.
while dier_leeft:
    # Teken een rechthoek om de schildpad (voor debugging).
    pygame.draw.rect(screen, (100, 100, 100), schildpad_rechthoek, 1)

    # Werk het scherm bij en vul de achtergrond met wit.
    pygame.display.flip()
    screen.fill(background_color)

    # Teken de schildpad en de sla op het scherm.
    screen.blit(schildpad, schildpad_rechthoek)
    screen.blit(sla, sla_rechthoek)

    # Print het huidige hongerniveau van de schildpad.
    print(f'ik heb zoveel honger: {honger}')

    # Verhoog de honger van de schildpad.
    honger = honger + 0.1

    # Controleer of de honger groter is dan 500. Als dat zo is, sterft de schildpad.
    if honger > 100: #aangepast om demonstratie vlotter af te kunnen ronden
        dier_leeft = False

    # Haal muisinvoer op (wordt niet gebruikt in deze code).
    pygame.event.get()
    locatie_muis = pygame.mouse.get_pos()
    knoppen = pygame.mouse.get_pressed()
    
    if knoppen[0] == 1:  # Controleer of de linkermuisknop is ingedrukt.
        if sla_rechthoek.collidepoint(locatie_muis):  # Controleer of de muis op de sla is.
            print('Haphap')  # Geef een melding in de console.
            honger = honger - 10  # Verminder de honger.

    # Verhoog de spring-teller. Als deze 10 bereikt, springt de sla naar een nieuwe, willekeurige positie.
    spring_teller = spring_teller + 1
    if spring_teller == 10:
        sla_rechthoek.center = (random.randint(0, breedte), random.randint(0, hoogte))
        spring_teller = 0

    # Maak de schildpad kleiner naarmate hij meer honger heeft.
    center = schildpad_rechthoek.center
    print(center)  # Print de huidige positie van de schildpad.
    schildpad = pygame.transform.rotozoom(schildpad_origineel, 0, (100 - honger) / 100)
    schildpad_rechthoek = schildpad.get_rect()
    schildpad_rechthoek.center = center

    # Controleer of de schildpad de rand van het scherm raakt en verander dan van richting.
    if schildpad_rechthoek.top < 0:  # Bovenkant van het scherm.
        schildpad_snelheid[1] = -schildpad_snelheid[1]
        schildpad_origineel = pygame.transform.flip(schildpad_origineel, True, False)

    if schildpad_rechthoek.bottom > 300:  # Onderkant van het scherm.
        schildpad_snelheid[1] = -schildpad_snelheid[1]
        schildpad_origineel = pygame.transform.flip(schildpad_origineel, True, False)

    if schildpad_rechthoek.left < 0:  # Linkerkant van het scherm.
        schildpad_snelheid[0] = -schildpad_snelheid[0]
        # Flip de schildpad horizontaal als hij omdraait.
        schildpad_origineel = pygame.transform.flip(schildpad_origineel, True, False)

    if schildpad_rechthoek.right > 600:  # Rechterkant van het scherm.
        schildpad_snelheid[0] = -schildpad_snelheid[0]
        # Flip de schildpad horizontaal als hij omdraait.
        schildpad_origineel = pygame.transform.flip(schildpad_origineel, True, False)

    # Beweeg de schildpad op basis van zijn snelheid.
    schildpad_rechthoek = schildpad_rechthoek.move(schildpad_snelheid)

    # Wacht een korte tijd voordat de volgende iteratie start.
    time.sleep(0.1)

# Print een bericht als de schildpad sterft.
print('Helaas, je schildpad is overleden')
