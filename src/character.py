#character class file
import helpers, random

class Character:
    def __init__(self):
        self.skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
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
        self.skill={list(self.skills[clas].keys())[0]:self.skills[clas][list(self.skills[clas].keys())[0]]}
        self.holds={}
        self.level=1

    def dictify(self):
        return {self.name:[self.clas,self.str,self.spd,self.mag,self.skill,self.holds,self.level]}

    def __str__(self):
        #display name, class, and level of CHAR
        print(f'\n{self.name}\nLevel {self.level} {self.clas}\n')
        #display attribute scores
        print(f'Strength: {self.str}\nSpeed: {self.spd}\nIntelligence: {self.mag}\n')
        #display skills in CHAR
        print(f'Active skill:\n{list(self.skill.keys())[0]}: {list(self.skill.values())[0]}\n')
        #display inventory of CHAR
        print('Inventory:')
        for i in self.holds.keys():
            print(f'{i}:\n{self.holds[i]}')
        if list(self.holds.keys())==[]:
            print('Inventory empty.')
    
    def sshow(self):
        return f'\n{self.name}\nLevel {self.level} {self.clas}\n'
    
    def level_up(self):
        #if CHAR is second level
        if self.level==2:
            #display character is max level
            print(f'\n{self.name} is max level.')
            return
        #set CHAR level to 2
        self.level=2
        #add function distribute called on random number between 5 and 10 to CHAR scores
        distr=helpers.distribute(random.randint(5,10))
        self.str+=distr[0]
        self.spd+=distr[1]
        self.mag+=distr[2]
        #display all skills in SKILLS that are for CHAR class
        print('\nSkills Avaliable:')
        for i,x in self.skills[self.clas].items():
            print(f'{i}: {x}')
        #set skill in CHAR to (valid) user input for which skill they want
        skil=helpers.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
        while skil not in ['1','2']:
            print('\nInvalid input. Try again.')
            skil=helpers.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
        if skil=='1':
            self.skill=list(self.skills[clas].keys())[0]:self.skills[clas][list(self.skills[clas].keys())[0]]
        elif skil=='2':
            modify(4,{list(skills[char[name][0]].keys())[1]:skills[char[name][0]][list(skills[char[name][0]].keys())[1]]})