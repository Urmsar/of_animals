# TODO: File with classes should be named a parent class - animal.py

class Animal:

    # TODO: We should leave on empty line after class definition.
    #  Fix the rest
    # TODO: It is better to format a large arguments list vertically
    def __init__(
            self,
            name,
            species,
            color,
            weight,
            lifetimes,
            description
    ):
        self.name = name
        self.species = species
        self.color = color
        self.weight = weight
        self.lifetimes = lifetimes
        self.description = description

    def init(self, **kwargs):
        self.__dict__.update(kwargs)

    # TODO: Very good!
    def get_species(self):
        return self.species

    def get_weight(self):
        return self.weight

    def get_lifetimes(self):
        return self.lifetimes

    def get_description(self):
        return self.description

    def __repr__(self):
        return self.name

    # TODO: We never print anything in the method.
    #  Method should return something back, just like you did above
    # TODO: It means that we change the name of the method: get_details()
    def print_details(self):
        print(self.name.upper())
        # TODO: The line was too long. Better to break it like this
        print(
            f'Species: {self.species}, weight: '
            f'{self.weight} kg, lifetimes: {self.lifetimes} years'
        )
        print('Description:', self.description)
        print()


# TODO: Do not leave commented out code during the code review
# special_features = {}

# TODO: Class name is always singular! Amphibian, Invertebrate etc. Fix it
class Invertebrates(Animal):
    def __init__(self, can_see, **kwargs):
        super().__init__(**kwargs)
        self.can_see = can_see

    # TODO: Should be named like get_special_features(self)
    def special_features(self):
        # TODO: Better to form this return as a f-string. Fix the rest
        return f'can_see {self.can_see}'


class Fish(Animal):
    def __init__(self, swim_bladder, **kwargs):
        super().__init__(**kwargs)
        # TODO: Very good!
        self.swim_bladder = swim_bladder

    def special_features(self):
        return 'swim_bladder', self.swim_bladder


class Amphibians(Animal):
    def __init__(self, tail, **kwargs):
        super().__init__(**kwargs)
        self.tail = tail

    def special_features(self):
        return 'tail', self.tail


class Reptiles(Animal):
    def __init__(self, amount_of_legs, **kwargs):
        super().__init__(**kwargs)
        self.amount_of_legs = amount_of_legs

    def special_features(self):
        return 'amount_of_legs', self.amount_of_legs


class Birds(Animal):
    def __init__(self, can_fly, **kwargs):
        super().__init__(**kwargs)
        self.can_fly = can_fly

    def special_features(self):
        return 'can_fly', self.can_fly


class Mammals(Animal):
    def __init__(self, live_in_water, **kwargs):
        super().__init__(**kwargs)
        self.live_in_water = live_in_water

    def special_features(self):
        return 'live_in_water', self.live_in_water
