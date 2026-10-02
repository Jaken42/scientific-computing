import sympy as sp

people = ["Alice", "Boris", "Charles", "Doris"]
positions = ["Manager", "Programmer", "Designer", "Marketing Expert"]
snacks = ["Apples", "Bananas", "Chips", "Donuts"]

def find_solution():
    for position_permutation in sp.utilities.iterables.multiset_permutations(positions):
        for snack_permutation in sp.utilities.iterables.multiset_permutations(snacks):
            position_of = dict(zip(people, position_permutation))
            snack_of = dict(zip(people, snack_permutation))

            # Reverse lookup
            person_with_position = {pos: person for person, pos in position_of.items()}

            if snack_of[person_with_position["Manager"]] != "Donuts":
                continue

            if position_of["Alice"] in ("Manager", "Marketing Expert"):
                continue

            if position_of["Boris"] not in ("Programmer", "Marketing Expert"):
                continue

            if snack_of[person_with_position["Designer"]] == "Chips":
                continue

            if snack_of["Charles"] != "Apples":
                continue

            if snack_of[person_with_position["Programmer"]] != "Bananas":
                continue

            return (position_of, snack_of)

solution = find_solution()

if solution is None:
    print("No solution found.")
else:
    for person in people:
        print(f"{person} is the {solution[0][person]} and likes {solution[1][person]}\n")