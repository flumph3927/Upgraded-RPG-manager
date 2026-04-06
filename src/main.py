#main function
import files,helpers,character,randoms,graphs

#create main function
def main():
    chars=files.load('docs/chars.json')
    #loop
    while True:
        #get user input for show character, compare characters, create character, modify character, view all characters, characters analytics, save, export, import, exit
        choice=input('1. Show character\n2. Compare character\n3. Create character\n4. Modify character\n5. View all characters\n6. Character analytics\n7. Save\n8. Export\n9. Import\n10. Exit\n')
        while choice not in [str(x+1) for x in range(10)]:
            print('Invalid input. Try again.')
            choice=input('1. Show character\n2. Compare character\n3. Create character\n4. Modify character\n5. View all characters\n6. Character analytics\n7. Save\n8. Export\n9. Import\n10. Exit\n')
        #if show character
        if choice=='1':
            choic=input('1. Comprehensive view\n2. Score visualization\n')
            while choic not in ['1','2']:
                print('Invalid input. Try again.')
                choic=input('1. Comprehensive view\n2. Score visualization\n')
            if choic=='1':
                char=helpers.select(chars)
                char.cshow()
            else:
                char=helpers.select(chars)
                graphs.DataVisualization(char).display()
        #else if compare characters
        elif choice=='2':
            char=helpers.select(chars)
            print('Choose second character:')
            char2=helpers.select(chars)
            graphs.DataVisualization(char,char2).compare()
        #else if create character
        elif choice=='3':
            #get user input for manual or random creation
            choic=input('1. Manual creation\n2. Randomize new character\n')
            while choic not in ['1','2']:
                print('Invalid input. Try again.')
                choic=input('1. Manual creation\n2. Randomize new character\n')
            #if manual
            if choic=='1':
                new=character.Character()
                chars[new.name]=new
            #else
            else:
                new=randoms.random_char()
                chars[new.name]=new
        #else if modify character
        elif choice=='4':
            #get user input for level up, change scores, change inventory, or change skill
            choic=input('1. Level up\n2. Change scores\n3. Modify inventory\n4. Change skill\n')
            while choic not in [str(x+1) for x in range(4)]:
                print('Invalid input. Try again.')
                choic=input('1. Level up\n2. Change scores\n3. Modify inventory\n4. Change skill\n')
            #if level up
            if choic=='1':
                char=helpers.select(chars)
                char.level_up()
                chars[char.name]=char
            #else if change scores
            elif choic=='2':
                char=helpers.select(chars)
                char.new_stats()
                chars[char.name]=char
            #else if change inventory
            elif choic=='3':
                char=helpers.select(chars)
                char.get_stuff()
                chars[char.name]=char
            #else
            else:
                char=helpers.select(chars)
                char.new_skill()
                chars[char.name]=char
        #else if view all
        elif choice=='5':
            helpers.display(chars)
        #else if character analytics
        elif choice=='6':
            framed=helpers.amalgamate(chars)
            #get user input for option: score information, class popularity, skill popularity
            choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
            while choic not in ['1','2','3']:
                print('Invalid input. Try again.')
                choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
            #if score information
            if choic=='1':
                #show mean,median,max,min among str,spd,mag
                print(f'Strength:\nMean: {framed.loc[1].mean()}\nMedian: {framed.loc[1].median()}\nMaximum: {framed.loc[1].max()}\nMinimum: {framed.loc[1].min()}\n')
                print(f'Speed:\nMean: {framed.loc[2].mean()}\nMedian: {framed.loc[2].median()}\nMaximum: {framed.loc[2].max()}\nMinimum: {framed.loc[2].min()}\n')
                print(f'Magic:\nMean: {framed.loc[3].mean()}\nMedian: {framed.loc[3].median()}\nMaximum: {framed.loc[3].max()}\nMinimum: {framed.loc[3].min()}\n')
            #else if class popularity
            elif choic=='2':
                #show classes and percentages from most to leasr self.skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
                kngt=framed.loc[0].eq('knight').sum()
                arcr=framed.loc[0].eq('archer').sum()
                wzrd=framed.loc[0].eq('wizard').sum()
                print(f'{kngt/(kngt+arcr+wzrd)*100}% of characters have the Knight class.\n{arcr/(kngt+arcr+wzrd)*100}% of characters have the Archer class.\n{wzrd/(kngt+arcr+wzrd)*100}% of characters have the Wizard class.')
            #else if skill popularity
            elif choic=='3':
                #do that ^ but with skills
                snipe=framed.loc[4].eq({'Snipe':'Ranged weapon range is doubled'}).sum()
                pa=framed.loc[4].eq({'Pierce Armor':'Double damage of ranged weapons.'}).sum()
                parry=framed.loc[4].eq({'Parry':'Use a melee attack to negate an enemy\'s next attack'}).sum()
                disarm=framed.loc[4].eq({'Disarm':'Use a melee attack to remove an enemy\'s weapon.'}).sum()
                qs=framed.loc[4].eq({'Quick Spell':'Cast two spells as one attack.'}).sum()
                cs=framed.loc[4].eq({'Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}).sum()
                print(f'Snipe: {snipe/(snipe+pa+parry+disarm+qs+cs)*100}%\nPierce Armor: {pa/(snipe+pa+parry+disarm+qs+cs)*100}%\nParry: {parry/(snipe+pa+parry+disarm+qs+cs)*100}%\nDisarm: {disarm/(snipe+pa+parry+disarm+qs+cs)*100}%\nQuick Spell: {qs/(snipe+pa+parry+disarm+qs+cs)*100}%\nChange Spell: {cs/(snipe+pa+parry+disarm+qs+cs)*100}%')
        #else if save
        elif choice=='7':
            files.save(helpers.amalgamate(chars),'docs/chars.json')
        #else if export
        elif choice=='8':
            #export all or single
            choic=input('1. Export all characters\n2. Export singular character\n')
            while choic not in ['1','2']:
                print('Invalid input. Try again.')
                choic=input('1. Export all characters\n2. Export singular character\n')
            if choic=='1':
                files.save(helpers.amalgamate(chars),input('File path to export to: '))
            else:
                char=helpers.select(chars)
                files.save(char.dtfrme(),input('File path to export to: '))
        #else if import
        elif choice=='9':
            try:
                files.load(input('File path to load from: '))
            except:
                print('Invalid file path')
        #else
        else:
            #break out of loop
            break

main()