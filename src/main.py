#main function
import files,helpers,character

#create main function
def main():
    chars=files.load('docs/chars.csv')
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
                pass
        #else if modify character
        elif choice=='4':
            #get user input for level up, change scores, change inventory, or change skill
            choic=input('1. Level up\n2. Change scores\n3. Modify inventory\n3. Change skill\n')
            while choic not in [str(x+1) for x in range(4)]:
                print('Invalid input. Try again.')
                choic=input('1. Level up\n2. Change scores\n3. Modify inventory\n3. Change skill\n')
            #if level up
            if choic=='1':
                char=helpers.select(chars)
                chars[char.name]=char.level_up()
            #else if change scores
            elif choic=='2':
                char=helpers.select(chars)
                chars[char.name]=char.new_stats()
            #else if change inventory
            elif choic=='3':
                char=helpers.select(chars)
                chars[char.name]=char.get_stuff()
            #else
            else:
                char=helpers.select(chars)
                chars[char.name]=char.new_skill()
        #else if view all
        elif choice=='5':
            helpers.display(chars)
        #else if character analytics
        elif choice=='6':
            pass
        #else if save
        elif choice=='7':
            files.save(helpers.amalgamate(chars),'docs/chars.csv')
        #else if export
        elif choice=='8':
            files.save(helpers.amalgamate(chars),input('File path to export to: '))
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