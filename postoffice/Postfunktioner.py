
def brev_kuvert(bredd, langd, tjocklek, vikt):
    """
    :param bredd: Skriv nu i bredd i cm
    :param langd: Skriv nu i langd i cm
    :param tjocklek: Skriv nu i tjockleken i cm
    :param vikt: Skriv slutligen in vikt i gram
    :return: Att du far eller inte far skicka ett kuvert med matten
    """
    if (bredd + langd + tjocklek) > 90:
        print("Du far inte skicka brevet, det ar for stort")
    elif bredd < 9:
        print("Brevet ar for smalt")
    elif langd < 14:
        print("Brevet ar for kort")
    elif langd > 60:
        print("Brevet ar for langt")
    elif vikt > 2000:
        print("Brevet vager for mycket")
    elif bredd < 0 or langd < 0 or tjocklek < 0 or vikt < 0:
        print("SKRIV IN RIKTIGA ENHETER OVER 0")
    else:
        if bredd > 25:
            print("Det tillkommer extra kostnader for bred over 25 cm")
        if tjocklek > 3:
            print("Det tillkommer extra kostnader for tjocklek over 3 cm")
        print("Du kan skicka ditt brev")

def brev_rulle(diameter, vikt, langd):
    """
    :param diameter: Skriv in diameter i cm
    :param vikt: Skriv in vikt i gram
    :param langd: Skriv in langd i cm
    :return: Om du far skicka ett brev i rulle eller ej
    """
    if (langd + (diameter*2)) > 104:
        print("Du far inte skicka rullen, det ar for stort")
    elif (langd + (diameter*2)) < 17:
        print("Du far inte skicka rullen det ar for litet")
    elif langd < 10:
        print("Rullen ar for kort")
    elif langd > 90:
        print("Rullen ar for langt")
    elif vikt > 2000:
        print("Rullen vager for mycket")
    else:
        print("Du kan skicka din rulle")

def paket_kartong_inrike(bredd, langd, hojd, vikt):
    """

    :param bredd: Skriv bredd i cm
    :param langd: Skriv langd i cm
    :param hojd: Skriv hojd i cm
    :param vikt: Skriv vikt i kg
    :return: Om du kan skicka paketet inrikes eller ej
    """

    if vikt > 20:
        print("Paketet vager for mycket")
    elif langd > 150:
        print("Du far inte skicka paketet, det ar for langt")
    elif bredd > 70:
        print("Paketet har for stor bredd for att kunna skickas")
    elif hojd > 115:
        print("Paketet ar for hogt")
    else:
        if langd > 120:
            print("Det tillkommer extra kostnader for langden")
        if  (langd + bredd + bredd + hojd + hojd) > 200:
            print("Extra kostnader kan tillkomma om du ar direktbetalande kund da paketet ar sa stort")
        print("Du kan nu skicka ditt paket i kartong")

def paket_kartong_utrike(bredd, langd, hojd, vikt):
    """

    :param bredd: Skriv bredd i cm
    :param langd: Skriv langd i cm
    :param hojd: Skriv hojd i cm
    :param vikt: Skriv vikt i kg
    :return: Om du kan skicka paketet utrikes eller ej
    """

    if vikt > 31.5:
        print("Paketet vager for mycket")
    elif langd > 150:
        print("Du far inte skicka paketet, det ar for langt")
    elif bredd > 70:
        print("Paketet har for stor bredd for att kunna skickas")
    elif hojd > 115:
        print("Paketet ar for hogt")
    else:
        if langd > 120:
            print("Det tillkommer extra kostnader for langden")
        if  (langd + bredd + bredd + hojd + hojd) > 200:
            print("Extra kostnader kan tillkomma om du ar direktbetalande kund da paketet ar sa stort")
        print("Du kan nu skicka ditt paket i kartong")

def paket_rulle_inrike(langd, diameter, vikt):
    """
    :param langd: Skriv langd i cm
    :param diameter: Skriv diameter i cm
    :param vikt: Skriv Vikt i Kg
    :return: Om du far skicka ditt paket i rulle eller ej
    """
    if vikt > 20:
        print("Paketet vager for mycket")
    elif langd > 150:
        print("Paketet ar for langd")
    elif diameter > 115:
        print("Paketet har for stor diameter")
    if langd > 120:
        print("Extra avigfter tillkommer for langd over 120")
    print("Du kan skicka din rulle")

def paket_rulle_utrike(langd, diameter, vikt):
    """
    :param langd: Skriv langd i cm
    :param diameter: Skriv diameter i cm
    :param vikt: Skriv Vikt i Kg
    :return: Om du far skicka ditt paket i rulle eller ej
    """
    if vikt > 20:
        print("Paketet vager for mycket")
    elif langd > 150:
        print("Paketet ar for langd")
    elif diameter > 115:
        print("Paketet har for stor diameter")
    if langd > 120:
        print("Extra avigfter tillkommer for langd over 120")
    print("Du kan skicka din rulle")

def pall_hel_inrike(langd, bredd, hojd, vikt):
    """
    :param langd: skriv in langd i cm
    :param bredd: Skriv in bredd i cm
    :param hojd: Skriv in hojd i cm
    :param vikt: Skriv in vikt i Kg
    :return: Om du far skicka pallen eller ej
    """