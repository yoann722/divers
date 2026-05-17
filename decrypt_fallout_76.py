from itertools import product
def decrypt(mot_decrypt,lettre_chiffre):
    comp = ''
    listechiffre = []
    listemot = []
    listebon = []
    nouveaumot=''
    dico_lettre_chiffre={}
    convertir={}
    alphabet_fondue=''
    mot_decrypt_fondue=''
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    alphabet_fondue=mot_decrypt+alphabet
    for enleve in alphabet_fondue: #enlever les lettres en trop
        if enleve not in mot_decrypt_fondue:
            mot_decrypt_fondue+=enleve
    #print(mot_decrypt_fondue)
    #ajout des lettres pour la conversion dans un dico
    for tours in range(26) :
        convertir.update({alphabet[tours]:mot_decrypt_fondue[tours]})
    #print(convertir)
    #ajout lettre et chiffre dans le second dico
    for x in range(0,15,2) :
        dico_lettre_chiffre.update({lettre_chiffre.lower()[x]:lettre_chiffre[x+1]})
    for recherche in dico_lettre_chiffre.keys() :
        for a,b in convertir.items() :
            if b == recherche:
                nouveaumot +=  a
    print(nouveaumot)
    #anagramme du mot
    liste = list(product(nouveaumot, repeat=8))
    for regroupe in  liste:
        if sorted(regroupe) == sorted(list(nouveaumot)):
            for ass in regroupe:
                comp+=ass
            listemot.append(comp)
            comp=''
    print(listemot)
    with open("aa.txt",'r',encoding="utf8") as ouverture:
        listefichier=ouverture.readlines()
        temp = [m.strip('\n') for m in listefichier]
        for p in listemot:
            if p in temp:
                listebon.append(p)
        ouverture.close()
    print('list anagamme',listebon)
    #conversion alphabet vers mot
    for anagramme in listebon:
        anagramme_decrypt = ''
        chiffre_decrypt = ''
        for lettre_anagramme in anagramme: # conversion alphabet vs base chiffrement
            anagramme_decrypt+=convertir[lettre_anagramme]
        for conv_chiffre in anagramme_decrypt: #conversion base chiffrement numero
            chiffre_decrypt+=dico_lettre_chiffre[conv_chiffre]
       
        listechiffre.append(chiffre_decrypt)
    print(listechiffre)
print('mot de decryptage')
mot=str(input())
print("saisir les lettre et chiffre comme ceci P1R4F8S9Z2D7")
angers=str(input())
decrypt(mot,angers)



