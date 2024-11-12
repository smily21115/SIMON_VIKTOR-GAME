import random as rand
import time
monsterdead = False
class Player:
    def __init__(self,HP,STR,INV,LVL,RUM,XP):
        self.HP = HP
        self.STR = STR
        self.INV = []
        self.LVL = LVL
        self.RUM = RUM
        self.XP = XP


class Enemies:
    def __init__(self,MHP,MSTR):
        self.MHP = rand.randint(1,spelare.HP)
        self.MSTR = rand.randint(1,spelare.STR)


class Items:
    def __init__(self,namn,beskriv,anvanda,STR_bonus,slitstyrk):
        self.namn = namn
        self.beskriv = beskriv
        self.anvanda = anvanda
        self.STR_bonus = STR_bonus
        self.slitstyrk = slitstyrk


class Room:
    def __init__(self,namn,beskrivn,kista):
        self.namn = namn
        self.beskrivn = beskrivn
        self.kista = kista


def STRBONUS(f1,f2):
    if rand.randint(1,10) >= 9:
        bonus = rand.randint(f1, f2)
    else:
        bonus = 0
    return bonus
def chestIn():
    if rand.randint(1,11) <= 6:
        return True
    else:
        return False
def chestInMellan():
    if rand.randint(1,50) >= 40:
        return True
    else:
        return False
def chestItems(f3,f4):
    i = rand.randint(f3,f4)
    if i >= 1:
        return rostigt_svard
    elif i == f4:
        return stal_svard
def dmgIntM(dmg):
    dmg = rand.randint((spelare.STR - 3), spelare.STR + 2)
    return dmg
def HPint():
    HP = rand.randint((spelare.HP - 3), spelare.HP + 3)
    return HP
def dmgS():
    if len(spelare.INV) > 0:
                    dmgS = (spelare.STR -1, spelare.STR + 1) + spelare.INV[-1].STR_bonus
    else:
        dmgS = rand.randint(spelare.STR -1, spelare.STR + 1)
    return dmgS


#Items


rostigt_svard = Items("Rostigt Svärd","Rostigt och trubbigt",True,STRBONUS(1,5),rand.randint(2,5))


stal_svard = Items("Svärd","Dammigt men fint skick, perfekt mot monster",True,STRBONUS(1,10),rand.randint(2,7))


damascus_svard = Items("Unikt svärd","Svärd gjort av olika metaller som skapar ett fantastiskt mönster. Slitstyrkan är unikt",True,STRBONUS(1,15),rand.randint(5,10))


hephaestus_svard = Items("Unikt svärd","Glänser som om den smeds i samma stund som du hittade den. Är detta Guds gåva?",True,STRBONUS(6,17),rand.randint(6,12))


#Rum


start_rum = Room("Start rum","","")


monster_rum = Room("Monster rum", "Det är mörkt, men det hörs att något andas.\n Det blir tyst... \n Ett öga lyser upp rummet och du ser...\n  \nEtt monster, DÖDA DET!",chestIn())


tomt_rum = Room("Tomt", "En fackla lyser upp rummet, men inget annat, tror jag", chestIn())


katt_rum = Room("Katt Rum", "Det är mörkt, men det hörs att något andas.\n Det blir tyst... \nEtt öga lyser upp rummet och du ser...\n \nEn katt!",chestIn())


mellanrum_monster = Room("MellanM", "Du klarade dig, bra att det finns en eld att värma dig.\n Använd kött du fick av besten eller drycker för att få tillbaka hälsa. Ett nytt rum väntar på dig...",chestInMellan())


mellanrum = Room("Mellan", "Kolla ditt inventory och hälsa, kanske en dryck som behövs?",chestInMellan())


#Player
spelare = Player(10,5,[],0,start_rum,0)


#Enemies






print("Du undrar kanske vart du är... \nTre rum väntar på dig, svaret till din fråga kan vara i ett av rummen...")
input("...")






while True:
    print("")
    print(spelare.RUM.beskrivn)
    a1 = rand.randint(1,20)
    w1 = rand.randint(1,20)
    d1 = rand.randint(1,20)
    antal = 0
    if a1 > 16:
        antal += 1
        a1 = monster_rum
    elif a1 > 14:
        antal += 1
        a1 = katt_rum
    elif a1 <= 14:
        a1 = tomt_rum
    if w1 > 16:
        antal += 1
        w1 = monster_rum
    elif w1 > 14:
        antal += 1
        w1 = katt_rum
    elif w1 <= 14:
        w1 = tomt_rum
    if d1 > 16:
        antal += 1
        d1 = monster_rum
    elif d1 > 14:
        antal += 1
        d1 = katt_rum
    elif d1 <= 14:
        d1 = tomt_rum
    if antal > 0:
        if antal == 1:
            antal = "ett"
        print(f"\nDet hörs något i {antal} av rummen...")
   
    time.sleep(1.5)
    d = input("Vilket av de tre rum vill du utforska?(a/w/d): ")
    if d == "a":
        d = a1
    if d == "w":
        d = w1
    if d == "d":
        d = d1
    spelare.RUM = d
    print(spelare.RUM.beskrivn)
    monsterdeadchest = False
    time.sleep(1)
    if spelare.RUM == monster_rum:
        monsterdead = False
        monsterdeadchest = False
        vap = chestItems(1,2).namn
        print(f"\nMonstret vrålar och tar fram ett {vap}")
        HPM = HPint()
        while monsterdead == False:
            print("Hur kommer du ta dig ann detta?\nSpringa iväg(-3HP, s),    ATTACK!(a)")
            enc = input("")
            if enc == "s":
                monsterdead = True
                monsterdeadchest = False
            if enc == "a":      print("Monstret rör sig mot dig med vapnet")
            while HPM > 0:
                print(HPM)
                HPM = HPM - dmgS()
            if HPM < 0:
                monsterdead = True
                monsterdeadchest = True
    if (d.kista == True) and (monsterdeadchest == True):
            print("Du ser en kista där också, villd u öppna den?(y/n)")
            if input() == "y":
                d.kista = spelare.INV.append(chestItems(1,4))
                c = spelare.INV[-1].namn
                print(f"Du hittade...\nEtt {c}")
           
                print(spelare.INV[-1].beskriv)


    print("\n")
    spelare.RUM = mellanrum