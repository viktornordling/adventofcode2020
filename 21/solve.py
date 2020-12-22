import math
from collections import deque


# Python program to find
# maximal Bipartite matching.

class Recipe:
    ingredients = []
    allergens = []

    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens


class GFG:
    def __init__(self, graph):

        # residual graph
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

        # A DFS based recursive function

    # that returns true if a matching
    # for vertex u is possible
    def bpm(self, u, matchR, seen):

        # Try every job one by one
        for v in range(self.jobs):

            # If applicant u is interested
            # in job v and v is not seen
            if self.graph[u][v] and seen[v] == False:

                # Mark v as visited
                seen[v] = True

                '''If job 'v' is not assigned to 
                   an applicant OR previously assigned  
                   applicant for job v (which is matchR[v])  
                   has an alternate job available.  
                   Since v is marked as visited in the  
                   above line, matchR[v]  in the following 
                   recursive call will not get job 'v' again'''
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen):
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        '''An array to keep track of the
           applicants assigned to jobs.
           The value of matchR[i] is the
           applicant number assigned to job i,
           the value -1 indicates nobody is assigned.'''
        matchR = [-1] * self.jobs

        # Count of jobs assigned to applicants
        result = 0
        for i in range(self.ppl):

            # Mark all jobs as not seen for next applicant.
            seen = [False] * self.jobs

            # Find if the applicant 'u' can get a job
            if self.bpm(i, matchR, seen):
                result += 1
        return matchR
        # return result


def solve_part_1(lines: list[str]):
    all_ingredients = set()
    all_allergens = set()
    all_recipes = []
    for line in lines:
        ingredients = line.split("(")[0].strip().split(" ")
        allergens = [a.strip() for a in line.split("contains")[1].split(")")[0].split(", ")]
        for ingredient in ingredients:
            all_ingredients.add(ingredient)
        for allergen in allergens:
            all_allergens.add(allergen)
        all_recipes.append(Recipe(ingredients, allergens))
    matrix = []
    ingr_list = list(all_ingredients)
    aller_list = list(all_allergens)
    ingr_map = {}
    reverse_ingr_map = {}
    aller_map = {}
    for index, ingr in enumerate(ingr_list):
        ingr_map[ingr] = index
    for index, ingr in enumerate(ingr_list):
        reverse_ingr_map[index] = ingr
    for index, aller in enumerate(aller_list):
        aller_map[aller] = index

    for _ in range(len(all_ingredients)):
        zero_list = [0 for _ in all_allergens]
        matrix.append(zero_list)

    # Strategy: for each allergen, find all recipes which mention that allergen.
    # The only ingredients that can contain that allergen are the ingredients that
    # appear in _all_ those recipes, so the intersection of all those sets.
    allergen_to_possible_ingredients = {}
    for a in all_allergens:
        ingredients_lists_mentioning_allergen = []
        for r in all_recipes:
            if a in r.allergens:
                ingredients_lists_mentioning_allergen.append(r.ingredients)
        sets = [set(ll) for ll in ingredients_lists_mentioning_allergen]
        intersection = set.intersection(*sets)
        allergen_to_possible_ingredients[a] = intersection

    for r in all_recipes:
        for i in r.ingredients:
            ingredient_id = ingr_map[i]
            for a in r.allergens:
                possible = allergen_to_possible_ingredients[a]
                allergen_id = aller_map[a]
                if i in possible:
                    matrix[ingredient_id][allergen_id] = 1
    g = GFG(matrix)
    foods_with_allergens_ids = g.maxBPM()
    foods_with_allergens = []
    for f in foods_with_allergens_ids:
        print("{} has an allergen".format(reverse_ingr_map[f]))
        foods_with_allergens.append(reverse_ingr_map[f])
    all_ingrs_set = set(all_ingredients)
    ingrs_without_allergens = all_ingrs_set - set(foods_with_allergens)
    print(ingrs_without_allergens)

    count = 0
    for r in all_recipes:
        for i in r.ingredients:
            if i in ingrs_without_allergens:
                count += 1
    return count


def solve_part_2(lines: list[str]):
    all_ingredients = set()
    all_allergens = set()
    all_recipes = []
    for line in lines:
        ingredients = line.split("(")[0].strip().split(" ")
        allergens = [a.strip() for a in line.split("contains")[1].split(")")[0].split(", ")]
        for ingredient in ingredients:
            all_ingredients.add(ingredient)
        for allergen in allergens:
            all_allergens.add(allergen)
        all_recipes.append(Recipe(ingredients, allergens))
    matrix = []
    ingr_list = list(all_ingredients)
    aller_list = list(all_allergens)
    ingr_map = {}
    reverse_ingr_map = {}
    reverse_aller_map = {}
    aller_map = {}
    for index, ingr in enumerate(ingr_list):
        ingr_map[ingr] = index
    for index, ingr in enumerate(ingr_list):
        reverse_ingr_map[index] = ingr
    for index, aller in enumerate(aller_list):
        aller_map[aller] = index
    for index, aller in enumerate(aller_list):
        reverse_aller_map[index] = aller

    for _ in range(len(all_ingredients)):
        zero_list = [0 for _ in all_allergens]
        matrix.append(zero_list)

    # Strategy: for each allergen, find all recipes which mention that allergen.
    # The only ingredients that can contain that allergen are the ingredients that
    # appear in _all_ those recipes, so the intersection of all those sets.
    allergen_to_possible_ingredients = {}
    for a in all_allergens:
        ingredients_lists_mentioning_allergen = []
        for r in all_recipes:
            if a in r.allergens:
                ingredients_lists_mentioning_allergen.append(r.ingredients)
        sets = [set(ll) for ll in ingredients_lists_mentioning_allergen]
        intersection = set.intersection(*sets)
        allergen_to_possible_ingredients[a] = intersection

    for r in all_recipes:
        for i in r.ingredients:
            ingredient_id = ingr_map[i]
            for a in r.allergens:
                possible = allergen_to_possible_ingredients[a]
                allergen_id = aller_map[a]
                if i in possible:
                    matrix[ingredient_id][allergen_id] = 1
    g = GFG(matrix)
    foods_with_allergens_ids = g.maxBPM()
    foods_with_allergens = []
    for f in foods_with_allergens_ids:
        print("{} has an allergen".format(reverse_ingr_map[f]))
        foods_with_allergens.append(reverse_ingr_map[f])
    assign_map = {}
    for aller_id, ingr_id in enumerate(foods_with_allergens_ids):
        print("aller_id {} is assigned to ingr_id {}".format(aller_id, ingr_id))
        print("aller {} is assigned to ingr {}".format(reverse_aller_map[aller_id], reverse_ingr_map[ingr_id]))
        assign_map[reverse_ingr_map[ingr_id]] = reverse_aller_map[aller_id]
    gg = [pair[0] for pair in sorted(assign_map.items(), key=lambda item: item[1])]
    print(",".join(gg))
    return "done"


def solve():
    lines = open('easy.txt', 'r').readlines()
    # lines = open('input.txt', 'r').readlines()
    # print("Part 1:", solve_part_1(lines))
    print("Part 2:", solve_part_2(lines))


solve()
