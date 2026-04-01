#character class file
import helpers, random, pandas

class Character:
    def __init__(self,opts=[]):
        self.skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
        if opts==[]:
            #make the user choose a name, and add it t the character dictionary as a key 
            name = input("What would you wish your character name to be?: ")
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
        else:
            self.name=opts[0]
            self.clas=opts[1]
            self.str=opts[2]
            self.spd=opts[3]
            self.mag=opts[4]
            self.skill=opts[5]
            self.holds=opts[6]
            self.level=opts[7]
    
    def dtfrme(self):
        return pandas.DataFrame({self.name:[self.clas,self.str,self.spd,self.mag,self.skill,self.holds,self.level]},index=['class','strength','speed','magic','skill','inventory','level'])

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
        self.str,self.spd,self.mag=helpers.distribute(random.randint(5,10))
        self.new_skill()

    def new_stats(self):
        #Display all of the main stats (Strength, speed, and intelligence) and there scores.
        print(f"Current scores:\nStrength: {self.str}\nSpeed: {self.spd}\nMagic: {self.mag}")
        self.str,self.spd,self.mag=helpers.distribute(self.str+self.spd+self.mag)
        print(f"New scores:\nStrength: {self.str}\nSpeed: {self.spd}\nIntelegence: {self.mag}")
    
    def new_skill(self):
        if self.level==1:
            print('You need to be level 2 to have multiple skill options.')
            return
        print('\nSkills Avaliable:')
        for i,x in self.skills[self.clas].items():
            print(f'{i}: {x}')
        #set skill in CHAR to (valid) user input for which skill they want
        skil=helpers.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
        while skil not in ['1','2']:
            print('\nInvalid input. Try again.')
            skil=helpers.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
        if skil=='1':
            self.skill={list(self.skills[self.clas].keys())[0]:self.skills[self.clas][list(self.skills[self.clas].keys())[0]]}
        elif skil=='2':
            self.skill={list(self.skills[self.clas].keys())[1]:self.skills[self.clas][list(self.skills[self.clas].keys())[1]]}
    
    def get_stuff(self):
        #Create a while loop for there choice
        while True:
            #ask them if they want to create a weapon or remove a weapon
            answer = helpers.simple(input("Would you like to create an item or destroy an item? (Please put c or d)"))
            #If there input equals create or remove, then break
            if answer == "c":
                break
            elif answer == "d":
                if self.holds != {}:
                    break
                else:
                    print('You have nothing to destroy.')
                    return
            #Else have continue
            else:
                print("That is not a correct option, please put c or d.(c for create, d for destroy)...")

        #Check to see which of the choices they choose

        #If they chose to add an item, let them create its name and its description, adding it to the dictionary
        if answer == "c":
            name = input("What is the name of this item?:")
            description = input("What is the description of this weapon?:")
            self.holds[name] = description
        #If they chose to remove an item, create a for loop that will print of the name and the description
        else:
            x = 1
            for key,value in self.holds.items():
                print(f"{x}. {key}: {value}\n")
                x += 1
        #Get valid user input
            while True:
                choice = helpers.simple(input("Which of the weapons do you want to remove? "))
                if choice in [str(x+1) for x in range(len(self.holds))]:
                    break
                else:
                    print(f"{choice} is not an option...")
        #Remove the choosen weapon
            del self.holds[list(self.holds.keys())[int(choice)-1]]