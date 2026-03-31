#character class file
import helpers, random

class character:
    def __init__(self):
        skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
        #make the user choose a name, and add it t the character dictionary as a key 
        name = helpers.simple(input("What would you wish your character name to be?: "))
        self.name = name
        #create a while loop
        while True:
        #make class equals input what their character class is going to be, with numbers to be easier, and stupid profe
            clas = input("\nPlease select the class you want to choose\n1:Archer\n2:Knight\n3:Wizard\n")
            if clas == "1" or clas == "2" or clas == "3":
                break
            else:
                print("Select again")
                continue
        if clas == "1":
            clas='archer'
            #add class to character information
            self.clas = clas
        elif clas == "2":
            clas='knight'
            #add class to character information
            self.clas = clas
        elif clas == "3":
            clas='wizard'
            #add class to character information
            self.clas = clas
        #print stats
        print("\nYour stats are:\nStrength\nSpeed\nMagic")
        #add stats to character information
        self.str, self.spd,self.mag = helpers.distribute(random.randint(5,10))
        #print skill and say that to unlock another one they need to level up
        print("\nYou have one skill right now, but if you level up, you will unlock more")
        #add skill to character information
        self.skill={list(skills[clas].keys())[0]:skills[clas][list(skills[clas].keys())[0]]}
        self.holds={}
        self.level=1

    def dictify(self):
        return {self.name:[self.clas,self.str,self.spd,self.mag,self.skill,self.holds,self.level]}