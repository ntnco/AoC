from aoc_get import get_input

inp = get_input()
#inp = '''mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
#trh fvjkl sbzzf mxmxvkd (contains dairy)
#sqjhc fvjkl (contains soy)
#sqjhc mxmxvkd sbzzf (contains fish)'''

inp = inp.splitlines()

class Food:
    def __init__(self, ings, allergs):
        self.ings = set(ings)
        self.allergs = set(allergs)

    def has_ing(self, ing):
        return ing in self.ings

    def has_allerg(self, allerg):
        return allerg in self.allergs

ingredients = set()
allergens = set()
food_list = []
all_ings_listed = []
for line in inp:
    ing_list, allerg_list = line.split(' (contains ')
    ing_list = ing_list.split(' ')
    print(len(ing_list))
    allerg_list = allerg_list[:-1].split(', ')

    for ing in ing_list:
        ingredients.add(ing)
    
    all_ings_listed.extend(ing_list)

    for allergen in allerg_list:
        allergens.add(allergen)

    f = Food(ing_list, allerg_list)
    food_list.append(f)

allerg_to_ing = {}

a = list(allergens)[0]
confirmed_bad = set()
for a in allergens:
    possible = ingredients.copy()
    for f in food_list:
        if f.has_allerg(a):
            possible &= f.ings
    print(a)
    print(possible)
    allerg_to_ing[a] = possible
    confirmed_bad |= possible

#to rewrite
good_ings = ingredients.copy()
for bad in confirmed_bad:
    good_ings.remove(bad)

p1 = 0
for good in good_ings:
    p1 += all_ings_listed.count(good)

print(p1)

allerg_list = list(allergens)
allerg_list.sort()
print(allerg_list)


# and I just did part2 with vim key strokes after that
