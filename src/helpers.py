def simple(input):
    input = (input).strip().lower()
    return input

def point_holder(total):
    def use_points(amount):
        nonlocal total
        total -= amount
        return total
    return use_points

#create function distribute, get POINTS
def distribute(points):
    #set SCORES to list of three 0s
    get_points=point_holder(points)
    scores=[0,0,0]
    #display you have POINTS points
    print(f'\nYou have {get_points(0)} points.')
    #get (valid) user input for how many points to put into strength
    while True:
        try:
            scor=int(simple(input('\nHow many points do you want to put into strength? ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                get_points(scor)
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to first in SCORES
    scores[0]+=scor
    #display you have POINTS points
    print(f'\nYou have {get_points(0)} points remaining.')
    #get (valid) user input for how many points to put into speed
    while True:
        try:
            scor=int(simple(input('\nHow many points do you want to put into speed? (The remaining points will go into magic) ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                get_points(scor)
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to second in SCORES
    scores[1]+=scor
    #display you have POINTS points put into intelligence
    print(f'\nThe remaining {get_points(0)} points go into magic.')
    #add POINTS to third in SCORES
    scores[2]+=get_points(0)
    #return SCORES
    return scores[0],scores[1],scores[2]