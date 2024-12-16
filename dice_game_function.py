import random # pattern 3.1

# these comments on patterns are notes for myself on what to include, I put comments next to what I saw as fulfilling each pattern

# patterns completed based on wc 2.0 (last graded assignment)
# pattern 1.1, 1.2, 2.1, 2.2, 3.1, 4.1, 4.2, 4.3, 4.4, 5.3, 8.1

# patterns needed to include based on wc 2.0 (last graded assignment)
# pattern 2.3, 2.4, 3.2, 4.5, 5.1, 5.2, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 7.4, 8.2, 8.3, 8.4

def dice_roll(dice_sides = 6): # pattern 2.3, 2.4
    """create a dice rolling game by typing in the number of sides, but if you do not type a side then it defaults to 6""" # pattern 8.2
    results_list = random.choices(range(1,dice_sides+1), k=3)
    return results_list

## tests
# random.seed(3)
# dice_roll(30)
# dice_roll(5)
# dice_roll(10)

def dice_checker(input): 
    """separates the numbers you can re-roll from the ones you cannot""" # pattern 8.2
    input_list = dice_roll()
    reroll_list = []
    cannot_reroll_list = []
    for number in input_list:
        if input_list.count(number) > 1:
            while input_list.count(number) > 0:
                input_list.remove(number)
                cannot_reroll_list.append(number)
    reroll_list = input_list
    print(input_list)
    print(f"Removed duplicates are:", cannot_reroll_list, "and cannot be re-rolled. The following numbers can be re-rolled:", reroll_list)

## tests
# dice_checker(dice_roll(6))
# dice_checker(dice_roll(4))
# dice_checker(5)
# dice_checker(3)