from animals import *

animals = [snail, wasp, eel, shark, frog, lizard, crocodile, viper, ostrich, parrot, whale, wolf, elephant, giraffe,
           monkey]
subclasses = Animal.__subclasses__()

print('This is animals list ')
for nr in range(0, len(animals)):
    print(nr + 1, "-", animals[nr])
print('and subclasses list ')
for nr in range(len(subclasses)):
    print("s" + str(nr + 1), "Subclass: -", subclasses[nr].__name__)
see_animals = True
while see_animals:
    answer = input(f'which animal show all details? 1..{len(animals)} or Q(uit) '
                   f'or L(ist) again? or to see animal in S+nr(Subclasses): ')
    if not answer:
        continue

    if answer.isdigit() and 0 < int(answer) <= len(animals):
        choice = animals[int(answer) - 1]
        choice.print_details()
    elif answer.upper() == "L":
        for nr in range(1, len(animals) + 1):
            print(nr, "-", animals[nr - 1])
        for nr in range(len(subclasses)):
            print("s" + str(nr + 1), "-", subclasses[nr].__name__)

    elif answer[0].upper() == "S":
        nr = int(answer[1]) - 1
        if 0 <= nr <= 6:
            print('Subclass -', subclasses[nr].__name__)
            choice = subclasses[nr]
            choice_animals = [animal for animal in animals if isinstance(animal, choice)]
            for animal in choice_animals:
                print(animal.name, end=': ', )
                print(animal.species, 'weight:', animal.weight, 'kg, lifetimes:', animal.lifetimes, 'y'
                                                                                                    ", special features:",
                      animal.special_features())
                print()
        else:
            continue
    elif answer.upper() == "Q":
        see_animals = False
