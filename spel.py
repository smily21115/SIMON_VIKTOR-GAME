import random as rand
import time
import json

class Player:
    def __init__(self,HP,STR,INV,INV_namn,INV_dur,LVL,RUM,XP,MAXHP,Gold,shop):
        self.HP = HP
        self.STR = STR
        self.INV = []
        self.INV_namn = []
        self.INV_dur = []
        self.LVL = LVL
        self.RUM = RUM
        self.XP = XP
        self.MAXHP = MAXHP
        self.Gold = Gold
        self.shop = ()
             
    def check_stats(self):
        print(f"---player stats---")
        print(f"{self.HP}HP/{self.MAXHP}HP")
        print(f"Strength {self.STR+equipped[0]}")
        print(f"Level {self.LVL}")
        print(f"{self.XP}XP / {self.get_next_level_xp()}XP")
        print(f"You have {self.Gold} Gold")
    
    def gain_xp(self,amount):
      self.XP += amount
      print(f"\nYou gained {amount} XP! Current XP: {self.XP}/{self.get_next_level_xp()}")

    def death(self):
        if self.HP<=0:
            print("you have now died restart the gane")
            exit()

    def gain_Gold(self,amount):
        self.Gold += amount
        print(f"\n You gained {amount} Gold you now have{self.Gold}")

    def get_next_level_xp(self):
        base_XP = 100
        scaling = 1.5
        return int(base_XP* (self.LVL**scaling))

    def level_up(self):
        self.LVL += 1
        self.MAXHP +=25   
        self.STR += 7  
        self.XP = 0  
        if self.LVL == 10:
            print("\nYou have reached level 10 and won the game! Congratulations!")
            exit()
            
    def open_shop(self):
        while True:
            print("\n --welcome to the shop--")
            print("1. Strength potion (150 Gold) - Increases your strength by an random ammount")
            print("2. Health potion (25 GOld) - Increases your HP by a minimum 10 up to your max HP ")
            print("3. Skill potion (50 Gold) - increases your wepons durabillity")
            print("4. exit the shop")
            
            choice = input("Choose an option (1-4): ")
            
            if choice == "1":
                if self.Gold >= 150:
                    self.Gold -= 150
                    str_increase = rand.randint(3, 8)  # Random boost
                    self.STR += str_increase
                    print(f"Your strength increased by {str_increase}! Current Strength: {self.STR}")
                    input(":")
                else:
                    print("You don't have enough Gold!")
                    input(":")
            elif choice == "2":
                if self.Gold >= 25:
                    self.Gold -= 25
                    heal = min(rand.randint(10, 25), self.MAXHP - self.HP)
                    self.HP += heal
                    print(f"You healed {heal} HP! Current HP: {self.HP}/{self.MAXHP}")
                    input(":")
                else:
                    print("You don't have enough Gold!")
                    input(":")
            elif choice == "3":
                if self.Gold >= 50:
                    if len(self.INV_dur) > 0:
                        self.Gold -= 50
                        self.INV_dur[equipped[4]] += 3
                        print(f"Durability of {self.INV_namn[equipped[4]].namn} increased to {self.INV_dur[equipped[4]]}")
                        input(":")
                    else:
                        print("You don't have any weapons to upgrade!")
                        input(":")
                else:
                    print("You don't have enough Gold!")
                    input(":")
            elif choice == "4":
                print("Exiting the shop...")
                return
            else:
                print("Invalid choice, please choose 1-4.")
                input(":")
    
        
class Enemies:
    def __init__ (self):
        self.MHP = rand.randint(100,50000) + (spelare.LVL*5)
        self.MSTR = rand.randint(5,10) + (spelare.LVL*3)
        #test för framtid funkar inte just nu

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

def STRBONUS(f1):
    if f1.namn == "Rostigt svärd":
        bonus = rand.randint(1,5)
    elif f1.namn == "Svärd":
        bonus = rand.randint(5,10)
    elif f1.namn == "Damascus svärd":
        bonus = rand.randint(10,20)
    elif f1.namn == "Gudomligt svärd":
        bonus = rand.randint(25,35)
    else:
        bonus = 1
    return bonus
        
def durFunk(f1):
    if f1.namn == "Rostigt svärd":
        dur = 7
    elif f1.namn == "Svärd":
        dur = 11
    elif f1.namn == "Damascus svärd":
        dur = 16
    elif f1.namn == "Gudomligt svärd":
        dur = 12
    return dur

def chestIn():
    if rand.randint(1,11) > 9:
        return True
    else:
        return False
def chestInMellan():
    if rand.randint(1,7) > 6:
        return True
    else:
        return False
def chestItems(f3,f4):
    i = rand.randint(f3,f4)
    if i <= 3:
        return rostigt_svard
    elif i >= f4:
        if (spelare.LVL >= 7) and (rand.randint(1,2) == 1):
            return hephaestus_svard
        if (spelare.LVL >= 3) and (rand.randint(1,2) == 1):
            return damascus_svard
        else:
            return stal_svard

def dmgIntM():
    dmg = rand.randint(int(spelare.STR/100), int(spelare.STR *1))
    return dmg

def HPint(ran):
    HP = ran
    return HP

def dmgS(strbonus):
    if strbonus > 0:
        dmgS = (rand.randint(int(spelare.STR/6), int(spelare.STR*1.4))) + strbonus
    else:
        dmgS = rand.randint(int(spelare.STR / 6), int(spelare.STR * 1.4))
    return dmgS

def vilketRum(awd):
    if awd > 14:
        awd = monster_rum
    elif awd >= 13:
        awd = trap_rum
    elif awd < 13:
        awd = tomt_rum
    return awd

def trapRum(rum):
    giftTid = int(rum+3)
    return giftTid
def monstantal(a,b,c):
    antal = 0
    if a > 14:
        antal += 1
    if b > 14:
        antal += 1
    if c > 14:
        antal += 1
    return antal

def equipFunk():
    myInt = False
    while myInt == False:
        vapen = input("Vilket vill du använda?(1,2,3...): ")
        if (vapen.isnumeric() == True):
            if int(vapen) <= len(spelare.INV) and int(vapen) > 0:
                equip = spelare.INV[int(vapen)-1]
                equip_namn = spelare.INV_namn[int(vapen)-1].namn
                durequip = spelare.INV_dur[int(vapen)-1]
                myInt = True
                vapen = int(vapen)-1
                vapen_list = [equip, equip_namn, True, durequip, vapen]
            else:
                print("Skriv in vilket vapen du vill använda(står under namnet och bonusen)")
        else:
            print("Skriv in vilket vapen du vill använda(står under namnet och bonusen)")
    return vapen_list

def bytaFunk(bon,namn,dura):
    myInt = False
    while myInt == False:
        vapen = input("Vilket vill du byta?: ")
        if (vapen.isnumeric() == True):
            if int(vapen) <= len(spelare.INV) and int(vapen) > 0:
                byta = spelare.INV[int(vapen)-1]
                spelare.INV.pop(int(vapen)-1)
                spelare.INV.append(bon)
                spelare.INV_namn.append(namn)  
                spelare.INV_dur.append(dura)
                myInt = True
            else:
                print("Skriv in vilket vapen du vill byta")
        else:
            print("Skriv in vilket vapen du vill byta")
    return byta
def durSvard(dur):
    dur = dur-1
    return dur
#Items


rostigt_svard = Items("Rostigt svärd","Rostigt och trubbigt",True,rand.randint(1,5),7)


stal_svard = Items("Svärd","Dammigt men fint skick, perfekt mot monster",True,10,11)


damascus_svard = Items("Damascus svärd","Svärd gjort av olika metaller som skapar ett fantastiskt mönster. Slitstyrkan är unikt",True,20,rand.randint(5,10))


hephaestus_svard = Items("Gudomligt svärd","Glänser som om den smeds i samma stund som du hittade den. Är detta Guds gåva?",True,30,rand.randint(6,12))


#Rum


start_rum = Room("Start rum","","")


monster_rum = Room("Monster rum", "Ett monster, DÖDA DET!",chestIn())


tomt_rum = Room("Tomt", "En fackla lyser upp rummet, men inget annat", chestIn())


trap_rum = Room("Trap Rum", "När du öppnar dörren så blir du träffad av en pil, du är nu förgiftad.",chestIn())


mellanrum_monster = Room("MellanM", "Du klarade dig, bra att det finns en eld att värma dig.\n Använd kött du fick av besten eller drycker för att få tillbaka hälsa. Ett nytt rum väntar på dig...",chestInMellan())


mellanrum = Room("Mellan", "Kolla ditt inventory och hälsa, kanske en dryck som behövs?",chestInMellan())


#Player
spelare = Player(25,5,[],[],[],1,start_rum,0,25,0,())

#Enemies


print("Du undrar kanske vart du är... \nTre rum väntar på dig, svaret till din fråga kan vara i ett av rummen...")
input("...")
antalRum = 0
equipped = [0,0,False,0]
tidGift = 0

while True:
    print("\n-------------\n")
    print(spelare.RUM.beskrivn)
    antal = 0
    if tidGift > antalRum:
        spelare.HP = spelare.HP - 2
        print("\n-------------")
        print("Du är förgiftad och förlorade två HP")
        print("\n-------------")
        if spelare.death() == True:
            print("You have now died pls restart the game")
            exit()
    a = rand.randint(1,20)
    w = rand.randint(1,20)
    d = rand.randint(1,20)
    a1 = vilketRum(a)
    w1 = vilketRum(w)
    d1 = vilketRum(d)
    antal = monstantal(a,w,d)
    
    if antal > 0:
        if antal == 1:
            antal = "ett"
        print(f"-------------!\nDet hörs något i {antal} av rummen...\n-------------!")
   
    d2 = False
    d3 = False
    while d3 == False:
        invordoor = input("Vill du utforska ett rum, kolla ditt inventory eller kolla dina stats eller köpa något från shop?(r/i/s/sh): ")
        if invordoor == "r":
            while d2 == False:
                d = input("\nVilket av de tre rum vill du utforska?(a/w/d): ")
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
        elif invordoor == "i":
            if len(spelare.INV) > 0:
                for value in range (0, len(spelare.INV)):
                    print("\n-------------")
                    print(f'{spelare.INV_namn[value].namn} som har strength bonus {spelare.INV[value]}')
                    print(f"({value+1})")
                    print("\n-------------")
                if len(spelare.INV) > 0:
                    equipped = equipFunk()
                    print(f"Du använder nu {equipped[1]} som har strength bonus {equipped[0]} och slitstyrkan {equipped[3]}")
                if antalRum > 0:
                    print(f"Du har gått igenom {antalRum} rum")
            else:
                print("Här fanns det inget")
            input(": ")
        elif invordoor == "s":
            spelare.check_stats()  
            input(": ")
        elif invordoor == "sh":
            spelare.open_shop()
            
            

    spelare.RUM = d  # Update the current room

    d.kista = chestIn()
    if (d == tomt_rum) and (d.kista == True):
        d.beskrivn = "En fackla lyser upp rummet"
    elif (d == tomt_rum) and (d.kista == False):
        d.beskrivn = "En fackla lyser upp rummet, men inget annat"
    print(spelare.RUM.beskrivn)
    monsterdeadchest = False
    time.sleep(1)
    if (d == trap_rum):
        forgiftad = True
        tidGift = trapRum(antalRum)

    if (d.kista == True) and (d == tomt_rum):
        print("Under facklan ser du en kista")
        print("Öppnar du den?(y/n): ")
        if input() == "y":
                appendThing = (chestItems(1,4))
                strengthbon = STRBONUS(appendThing)
                dur = durFunk(appendThing)
                if len(spelare.INV) <= 4:
                    spelare.INV_namn.append(appendThing)
                    spelare.INV.append(strengthbon)
                    spelare.INV_dur.append(dur)
                    print(f"Du hittade...\nEtt {spelare.INV_namn[-1].namn}") 
                    print(spelare.INV_namn[-1].beskriv)
                else:
                    print("Du har inte tillräckligt med plats i ditt inventory")
                    byte = input(f"Vill du byta ut något i ditt inventory mot {appendThing.namn} med strength bonusen {strengthbon}?(y/n): ")
                    if byte == "y":
                        for value in range (0, len(spelare.INV)):
                            print("\n-------------")
                            print(f'{spelare.INV_namn[value].namn} som har strength bonus {spelare.INV[value]}')
                            print(f"({value+1})")
                            print("\n-------------")
                        bytaFunk(strengthbon,appendThing,dur)
                input("\n:")

    if spelare.RUM == monster_rum:
        monsterdead = False
        monsterdeadchest = False
        vap = chestItems(1,2).namn
        print(f"\nMonstret vrålar och tar fram ett {vap}")
        HPM = HPint(rand.randint((spelare.MAXHP - 3), spelare.MAXHP + 3))
        
        while monsterdead == False:
            print("Hur kommer du ta dig ann detta?\nSpringa iväg(-3HP, s),    ATTACK!(a)")
            enc = input("")
            if enc == "s":
                monsterdead = True
                spelare.HP -= 3
                if spelare.death() == True:
                    print("You have now died pls restart the game")
                    exit()      
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
                            if equipped[2] == True:
                                dmgtomonster = dmgS(equipped[0])
                                HPM = HPM - dmgtomonster
                                val = True
                                spelare.INV_dur[equipped[4]] = durSvard(spelare.INV_dur[equipped[4]])
                                print(f"Du slängde ditt vapen mot monstret och skadade det med {dmgtomonster}\n-------------")
                                if spelare.INV_dur[equipped[4]] < 1:
                                    print("Ditt svärd gick sönder")
                                    spelare.INV.pop(equipped[4])
                                    spelare.INV_dur.pop(equipped[4])
                                    spelare.INV_namn.pop(equipped[4])
                            else:
                                dmgtomonster = dmgS(0)
                                HPM = HPM - dmgtomonster
                                val = True
                                print(f"Du slängde din hand mot monstret och skadade det med {dmgtomonster}\n-------------")
                            time.sleep(1.2)
                        if drag == "i":
                            if len(spelare.INV) > 0:
                                for value in range (0, len(spelare.INV)):
                                    print("\n-------------")
                                    print(f'{spelare.INV_namn[value].namn} som har strength bonus {spelare.INV[value]}')
                                    print(f"({value+1})")
                                    print("\n-------------")
                                if len(spelare.INV) > 0:
                                    equipped = equipFunk()
                                    print(f"Du använder nu {equipped[1]} som har strength bonus {equipped[0]}")
                            else:
                                print("Här fanns det inget")
                    if HPM > 0:
                        dmgtoplayer = dmgIntM()
                        spelare.HP = spelare.HP - dmgtoplayer
                        print(f"\nMonstret slänger vapnet mot dig och du förlorar {dmgtoplayer} hälsa")
                        time.sleep(1.2)
                        if spelare.death() == True:
                            print("You have now died pls restart the game")
                            exit()
                if HPM <= 0:
                    monsterdead = True
                    monsterdeadchest = True
                    
        if monsterdeadchest == True:
            print("you have killed the monster")
            XP = rand.randint(30,45)
            spelare.XP += XP
            Gold = rand.randint(70,170)
            spelare.Gold += Gold
            print(f"\n You gained {Gold} Gold, you now have {spelare.Gold} Gold")
            print(f"\n ")
            print(f"The mosnter dropped {XP}XP, you now have {spelare.XP}XP and need {spelare.get_next_level_xp()}XP to level up")
            if spelare.XP >= spelare.get_next_level_xp():
                spelare.level_up()
                print(f"You have leveld up to level {spelare.LVL}")
                
    if (d.kista == True) and (monsterdeadchest == True):
            print("Du ser en kista där också, vill du öppna den?(y/n)")
            if input() == "y":
                appendThing = (chestItems(1,4))
                strengthbon = STRBONUS(appendThing)
                dur = durFunk(appendThing)
                if len(spelare.INV) <= 4:
                    spelare.INV_namn.append(appendThing)
                    spelare.INV.append(strengthbon)
                    spelare.INV_dur.append(dur)
                    print(f"Du hittade...\nEtt {spelare.INV_namn[-1].namn}") 
                    print(spelare.INV_namn[-1].beskriv)
                else:
                    print("Du har inte tillräckligt med plats i ditt inventory")
                    byte = input(f"Vill du byta ut något i ditt inventory mot {appendThing.namn} med strength bonusen {strengthbon}?(y/n): ")
                    if byte == "y":
                        for value in range (0, len(spelare.INV)):
                            print("\n-------------")
                            print(f'{spelare.INV_namn[value].namn} som har strength bonus {spelare.INV[value]}')
                            print(f"({value+1})")
                            print("\n-------------")
                        bytaFunk(strengthbon,appendThing.namn,dur)
                input("\n:")


    print("\n")
    antalRum += 1
    spelare.RUM = mellanrum
    spelare.RUM.kista = chestInMellan()
    if spelare.RUM.kista == True:
        print("I mellanrummet är det en kista, vill du öppna den?(y/n): ")
        if input() == "y":
                appendThing = (chestItems(1,4))
                strengthbon = STRBONUS(appendThing)
                dur = durFunk(appendThing)
                if len(spelare.INV) <= 4:
                    spelare.INV_namn.append(appendThing)
                    spelare.INV.append(strengthbon)
                    spelare.INV_dur.append(dur)
                    print(f"Du hittade...\nEtt {spelare.INV_namn[-1].namn}") 
                    print(spelare.INV_namn[-1].beskriv)
                else:
                    print("Du har inte tillräckligt med plats i ditt inventory")
                    byte = input(f"Vill du byta ut något i ditt inventory mot {appendThing.namn} med strength bonusen {strengthbon}?(y/n): ")
                    if byte == "y":
                        for value in range (0, len(spelare.INV)):
                            print("\n-------------")
                            print(f'{spelare.INV_namn[value].namn} som har strength bonus {spelare.INV[value]}')
                            print(f"({value+1})")
                            print("\n-------------")
                        bytaFunk(strengthbon,appendThing,dur)
                input("\n:") 