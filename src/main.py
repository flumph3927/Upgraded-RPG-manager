#main function
import files,helpers,character,randoms

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
            pass
        #else if compare characters
        elif choice=='2':
            pass
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
                framed.loc(1).mean(axis=1,numeric_only=True)
                #show mean,median,max,min among str,spd,mag
                print(f'Strength:\nMean: {framed.loc(1).mean(axis=1,numeric_only=True)}\nMedian: {framed.loc(1).median(axis=1,numeric_only=True)}\nMaximum: {framed.loc(1).max(axis=1,numeric_only=True)}\nMinimum: {framed.loc(1).min(axis=1,numeric_only=True)}\n')
                print(f'Speed:\nMean: {framed.loc(2).mean(axis=1,numeric_only=True)}\nMedian: {framed.loc(2).median(axis=1,numeric_only=True)}\nMaximum: {framed.loc(2).max(axis=1,numeric_only=True)}\nMinimum: {framed.loc(2).min(axis=1,numeric_only=True)}\n')
                print(f'Magic:\nMean: {framed.loc(3).mean(axis=1,numeric_only=True)}\nMedian: {framed.loc(3).median(axis=1,numeric_only=True)}\nMaximum: {framed.loc(3).max(axis=1,numeric_only=True)}\nMinimum: {framed.loc(3).min(axis=1,numeric_only=True)}\n')
            #else if class popularity
                #show classes and percentages from most to leasr
            #else if skill popularity
                #do that ^ but with skills
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