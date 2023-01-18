from animal import Animal, Invertebrates, Fish, Amphibians, Reptiles, Birds, Mammals

wasp = Invertebrates(
    name='wasp',
    species='Yellowjacket',
    color='yellow',
    weight=0,
    lifetimes=1,
    can_see=True,
    description='The most commonly known wasps, such as yellowjackets and hornets, are in the family Vespidae '
                'and are eusocial, living together in a nest with an egg-laying queen and non-reproducing workers'
)

snail = Invertebrates(
    name='snail',
    species='Giant African Snail',
    color='dark gray',
    weight=0,
    lifetimes=3,
    can_see=False,
    description='Living snakes are found on every continent except Antarctica, and on most smaller land masses; '
                'exceptions include some large islands, such as Ireland, Iceland, Greenland, '
                'the Hawaiian archipelago, and the islands of New Zealand'
)

shark = Fish(
    name='shark',
    species='Ground sharks',
    color='gray',
    weight=2000,
    lifetimes=25,
    swim_bladder=False,
    description='They are distinguished by an elongated snout and a nictitating membrane '
                'which protects the eyes during an attack'
)

eel = Fish(
    name='eel',
    species='European eel',
    color='brown-grey',
    weight=6,
    lifetimes=85,
    swim_bladder=True,
    description='Eels have been important sources of food both as adults (including jellied eels '
                'of East London) and as glass eels.'
)

frog = Amphibians(
    name='frog',
    species='Salientia',
    color='yellow',
    weight=3,
    lifetimes=6,
    tail=False,
    description='Salientia (Latin salire (salio), "to jump") is the name of the total group that includes '
                'modern frogs in the order Anura as well as their close fossil relatives'
)
lizard = Amphibians(
    name='lizard',
    species='Eastern newt',
    color='dark-yellow',
    weight=0,
    lifetimes=10,
    tail=True,
    description='It frequents small lakes, ponds, and streams or nearby wet forests.'
)

crocodile = Reptiles(
    name='crocodile',
    species='Nile crocodile',
    color='gray',
    weight=414,
    lifetimes=80,
    amount_of_legs=4,
    description='Nile crocodiles are opportunistic apex predators; a very aggressive crocodile, '
                'they are capable of taking almost any animal within their range.'
)

viper = Reptiles(
    name='viper',
    species='Vipera berus',
    color='sik-sak',
    weight=2,
    lifetimes=25,
    amount_of_legs=0,
    description='All viperids have a pair of relatively long solenoglyphous (hollow) fangs that are used to inject '
                'venom from glands located towards the rear of the upper jaws'
)

ostrich = Birds(
    name='ostrich',
    species='North African ostrich',
    color='gray',
    weight=130,
    lifetimes=15,
    can_fly=False,
    description='An ostrich is a type of large flightless bird. '
                'The North African ostrich was the most widespread subspecies of ostrich.'
)

parrot = Birds(
    name='parrot',
    species='Australian ringneck',
    color='green',
    weight=1,
    lifetimes=70,
    can_fly=True,
    description='The subspecies of the Australian ringneck differ considerably in colouration. It is a medium size '
                'species around 33 cm long. The basic colour is green, and all four subspecies have the characteristic '
                'yellow ring around the hindneck; wings and tail are a mixture of green and blue.'
)

wolf = Mammals(
    name='wolf',
    species='Ethiopian wolf',
    color='dark gray',
    weight=40,
    lifetimes=20,
    live_in_water=False,
    description="The Ethiopian wolf,also called the Simien jackal and Simien fox, is a canine native "
                "to the Ethiopian Highlands."
)

whale = Mammals(
    name='whale',
    species='Blue whale',
    color='blue',
    weight=190000,
    lifetimes=80,
    live_in_water=True,
    description="Reaching a maximum confirmed length of 29.9 meters and weighing up to 199 tonnes, "
                "it is the largest animal known to have ever existed."
)

lion = Mammals(
    name='lion',
    species='Southern lion',
    color='yellow',
    weight=105,
    lifetimes=15,
    live_in_water=False,
    description="The lion, or lioness for females, is a large cat of the genus Panthera native "
                "to Africa and India. "
)
elephant = Mammals(
    name='elephant',
    species='African bush elephant',
    color='grey',
    weight=9000,
    lifetimes=70,
    live_in_water=False,
    description='The African bush elephant is one of two extant African elephant species and '
                'one of three extant elephant species. It is the largest living terrestrial animal.'
)
giraffe = Mammals(
    name='giraffe',
    species='Reticulated giraffe',
    color='orange',
    weight=200,
    lifetimes=60,
    live_in_water=False,
    description='The reticulated giraffe, also known as the Somali giraffe, is a subspecies or species of giraffe '
                'native to the Horn of Africa. It lives in Somalia, southern Ethiopia, and northern Kenya. '
)
monkey = Mammals(
    name='monkey',
    species='Geleda',
    color='brown',
    weight=15,
    lifetimes=55,
    live_in_water=False,
    description="The gelada is large and robust and it is covered with buff to dark brown, "
                "coarse hair and has a dark face with pale eyelids."
)

