def animal_calculator(heads: int, paws: int) -> int:
    bunnies = 4
    chickens = 2

    num_bunnies = (paws - (chickens * heads)) / 2
    num_chickens = heads - num_bunnies

    return {
        "chickens": num_chickens,
        "bunnies": num_bunnies
    }

print(animal_calculator(35,94))