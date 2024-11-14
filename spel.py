import random as rand
import time

class Player:
    def __init__(self,HP,STR,INV,LVL,RUM,XP):
        self.HP = HP
        self.STR = STR
        self.INV = []
        self.LVL = LVL
        self.RUM = RUM
        self.XP = XP

    def gain_xp(amount):
      spelare.XP += amount
      print(f"\nYou gained {amount} XP! Current XP: {spelare.XP}/{spelare.get_next_level_xp()}")

    def get_next_level_xp(spel):
        return 100 * spelare.LVL  

    def level_up(spal):
        spelare.LVL += 1
        spelare.HP += 10  
        spelare.STR += 5  
        spelare.XP = 0  

      
        if spelare.LVL == 10:
            print("\nYou have reached level 10 and won the game! Congratulations!")
            exit()

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
        #self.trap = trap

def STRBONUS(f1,f2):
    if rand.randint(1,10) >= 1:
        bonus = rand.randint(f1, f2)
    else:
        bonus = 1
    return bonus
def chestIn():
    if rand.randint(1,11) >= 9:
        return True
    else:
        return False
def chestInMellan():
    if rand.randint(1,5) <= 4:
        return True
    else:
        return False
def chestItems(f3,f4):
    i = rand.randint(f3,f4)
    if i <= 3:
        return rostigt_svard
    elif i == f4:
        return stal_svard
#def trapIn():

def dmgIntM():
    dmg = rand.randint((spelare.STR - 3), spelare.STR + 2)
    return dmg
def HPint(ran):
    HP = ran
    return HP
def dmgS(strbonus):
    if strbonus > 0:
        dmgS = (rand.randint(spelare.STR-1, spelare.STR+1)) + (strbonus)
    else:
        dmgS = rand.randint(spelare.STR -1, spelare.STR + 1)
    return dmgS
def vilketRum(awd):
    if awd > 16:
        awd = monster_rum
    elif awd > 14:
        awd = katt_rum
    elif awd <= 14:
        awd = tomt_rum
    return awd
def monkatan(a,b,c):
    antal = 0
    if a > 14:
        antal += 1
    if b > 14:
        antal += 1
    if c > 14:
        antal += 1
    return antal


#Items

rostigt_svard = Items("Rostigt svärd","Rostigt och trubbigt",True,5,rand.randint(2,5))


stal_svard = Items("Svärd","Dammigt men fint skick, perfekt mot monster",True,10,rand.randint(2,7))


damascus_svard = Items("Unikt svärd","Svärd gjort av olika metaller som skapar ett fantastiskt mönster. Slitstyrkan är unikt",True,20,rand.randint(5,10))


hephaestus_svard = Items("Unikt svärd","Glänser som om den smeds i samma stund som du hittade den. Är detta Guds gåva?",True,30,rand.randint(6,12))


#Rum


start_rum = Room("Start rum","","")


monster_rum = Room("Monster rum", "Det är mörkt, men det hörs att något andas.\n Det blir tyst... \n Ett öga lyser upp rummet och du ser...\n  \nEtt monster, DÖDA DET!",chestIn())


tomt_rum = Room("Tomt", "En fackla lyser upp rummet, men inget annat", chestIn())


katt_rum = Room("Katt Rum", "Det är mörkt, men det hörs att något andas.\n Det blir tyst... \nEtt öga lyser upp rummet och du ser...\n \nEn katt!",chestIn())


mellanrum_monster = Room("MellanM", "Du klarade dig, bra att det finns en eld att värma dig.\n Använd kött du fick av besten eller drycker för att få tillbaka hälsa. Ett nytt rum väntar på dig...",chestInMellan())


mellanrum = Room("Mellan", "Kolla ditt inventory och hälsa, kanske en dryck som behövs?",chestInMellan())


#Player
spelare = Player(10,5,[],1,start_rum,0)


#Enemies


print("Du undrar kanske vart du är... \nTre rum väntar på dig, svaret till din fråga kan vara i ett av rummen...")
input("...")

while True:
    print("\n-------------\n")
    print(spelare.RUM.beskrivn)
    antal = 0
    a = rand.randint(1,20)
    w = rand.randint(1,20)
    d = rand.randint(1,20)
    a1 = vilketRum(a)
    w1 = vilketRum(w)
    d1 = vilketRum(d)
    antal = monkatan(a,w,d)
    
    if antal > 0:
        if antal == 1:
            antal = "ett"
        print(f"Det hörs något i {antal} av rummen...")
   
    d2 = False
    d3 = False
    while d3 == False:
        invordoor = input("Vill du utforska ett rum eller kolla ditt inventory?(r/i): ")
        if invordoor == "r":
            while d2 == False:
                d = input("Vilket av de tre rum vill du utforska?(a/w/d): ")
                if d == "a":
                    d = a1
                    d2 = True
                    d3 = True
                elif d == "w":
                    d = w1
                    d2 = True
                    d3 = True
                elif d == "d":
                    d = d1
                    d2 = True
                    d3 = True
                else:
                    print("Skriv in, a, w eller d")
        if invordoor == "i":
            for value in spelare.INV:
                print("\n-------------")
                print(f'{value.namn} som har strength bonus {value.STR_bonus}')
                print("\n-------------")
            input("")
    spelare.RUM = d

    d.kista = chestIn()
    if (d == tomt_rum) and (d.kista == True):
        d.beskrivn = "En fackla lyser upp rummet"
    elif (d == tomt_rum) and (d.kista == False):
        d.beskrivn = "En fackla lyser upp rummet, men inget annat"
    print(spelare.RUM.beskrivn)
    monsterdeadchest = False
    time.sleep(1)
    if (d.kista == True) and (d != monster_rum) and (d != katt_rum):
        print("Under facklan ser du en kista")
        print("Öppnar du den?(y/n): ")
        if input() == "y":
                d.kista = spelare.INV.append(chestItems(1,4))
                c = spelare.INV[-1]
                print(f"Du hittade...\nEtt {c.namn}")
                spelare.INV[-1].STR_bonus = STRBONUS(2, c.STR_bonus)
                print(spelare.INV[-1].beskriv)

    if spelare.RUM == monster_rum:
        monsterdead = False
        monsterdeadchest = False
        vap = chestItems(1,2).namn
        print(f"\nMonstret vrålar och tar fram ett {vap}")
        HPM = HPint(rand.randint((spelare.HP - 3), spelare.HP + 3))
        
        while monsterdead == False:
            print("Hur kommer du ta dig ann detta?\nSpringa iväg(-3HP, s),    ATTACK!(a)")
            enc = input("")
            if enc == "s":
                monsterdead = True
                spelare.HP -= 3
            elif enc == "a":      
                print("Monstret rör sig mot dig med vapnet")
                while HPM > 0:
                    print("\n-------------")
                    print(f'Monstrets hälsa är: {HPM}')
                    print(f'Din hälsa är: {spelare.HP}')
                    print("\n-------------")
                    val = False
                    while val == False:
                        drag = input("\nÖppna inv(i)\nSlå ditt slag mot besten(a)\n: ")
                        if drag == "a":
                            if len(spelare.INV) > 0:
                                dmgtomonster = dmgS(spelare.INV[-1].STR_bonus)
                                HPM = HPM - dmgtomonster
                                val = True
                                print(f"Du slängde ditt vapen mot monstret och skadade det med {dmgtomonster}\n-------------")
                            else:
                                dmgtomonster = dmgS(0)
                                HPM = HPM - dmgtomonster
                                val = True
                                print(f"Du slängde ditt hand mot monstret och skadade det med {dmgtomonster}\n-------------")
                            time.sleep(1.2)
                        if drag == "i":
                            for value in spelare.INV:
                                print(f'{value.namn} som har strength bonus {value.STR_bonus}', end=' ')
                                input("\n")
                    if HPM > 0:
                        dmgtoplayer = dmgIntM()
                        spelare.HP = spelare.HP - dmgtoplayer
                        print(f"\nMonstret slänger vapnet mot dig och du förlorar {dmgtoplayer} hälsa")
                        time.sleep(1.2)
                if HPM <= 0:
                    monsterdead = True
                    monsterdeadchest = True
                    
        if monsterdeadchest == True:
            print("you have killed the monster")
            spelare.XP += rand.randint(10,25)
            print(f"{spelare.XP}/{spelare.get_next_level_xp()}XP")
            if spelare.XP >= spelare.get_next_level_xp():
                spelare.level_up()
                print(f"You have leveld up to level {spelare.LVL}")

 
                
    if (d.kista == True) and (monsterdeadchest == True):
            print("Du ser en kista där också, vill du öppna den?(y/n)")
            if input() == "y":
                d.kista = spelare.INV.append(chestItems(1,4))
                c = spelare.INV[-1]
                print(f"Du hittade...\nEtt {c.namn}")
                spelare.INV[-1].STR_bonus = STRBONUS(2, c.STR_bonus)
                print(spelare.INV[-1].beskriv)


    time.sleep(1)
    print("\n")
    spelare.RUM = mellanrum
    spelare.RUM.kista = chestInMellan()
    if spelare.RUM.kista == True:
        print("I mellanrummet är det en kista, vill du öppna den?(y/n): ")
        if input() == "y":
                d.kista = spelare.INV.append(chestItems(1,4))
                c = spelare.INV[-1]
                print(f"Du hittade...\nEtt {c.namn}")
                spelare.INV[-1].STR_bonus = STRBONUS(2, c.STR_bonus)
                print(spelare.INV[-1].beskriv)