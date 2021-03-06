import dog_names
import cat_names

pet_input = '''Which pet name you want?

[1] Dog
[2] Cat

Enter option number:- '''

gender_text = '''Which gender pet name you want?

[1] Male
[2] Female
[3] Any

Enter option number :- '''


def main():
    pet = int(input(pet_input))
    if pet not in [1, 2]:
        print('\nInvalid option\n')
    
    gender = int(input(gender_text))
    if gender not in [1, 2, 3]:
        print('\nInvalid option\n')

    if pet == 1:
        if gender == 1:
            name = dog_names.random(gender='male')
        elif gender == 2:
            name = dog_names.random(gender='female')
        else:
            name = dog_names.random()
    else:
        if gender == 1:
            name = cat_names.random(gender='male')
        elif gender == 2:
            name = cat_names.random(gender='female')
        else:
            name = cat_names.random()

    print('\nName :- '+name)


main()
