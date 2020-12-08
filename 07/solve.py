from math import prod
import re
import math
import string

def parse_contain(can):
    if can.strip() == "no other bags.":
        return {'amount': 0, 'bag_name': None}
    amount = can.strip().split(" ")[0]
    bag_name = " ".join(can.split(" ")[2:-1])
    return {'amount': amount, 'bag_name': bag_name}


def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s


def parse_rule(line):
    bag_name = rchop(line.split("contain")[0].strip()[0:-1], "bag").strip()
    can_contain = [parse_contain(can) for can in line.split("contain")[1].split(",")]
    return {'bag_name': bag_name, 'rule': can_contain}


# lines = open('easy.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()

bag_rules = [parse_rule(line) for line in lines]
bag_rule_dict = {bag_rule['bag_name']: bag_rule['rule'] for bag_rule in bag_rules}

bag_to_containable_bags = {}
for bag in bag_rules:
    for rule in bag['rule']:
        contained_bag = rule['bag_name']
        containable_bags = bag_to_containable_bags.get(contained_bag, [])
        containing_bag = bag['bag_name']
        containable_bags.append(containing_bag)
        bag_to_containable_bags[contained_bag] = containable_bags

def count_possible_outer_bags(start_bag):
    containable_bags = set(bag_to_containable_bags.get(start_bag, []))
    further = set()
    for bag in containable_bags:
        further |= count_possible_outer_bags(bag)
    return containable_bags | further

def count_bags_in(start_bag):
    rule = bag_rule_dict.get(start_bag, None)
    if rule is None:
        return 1
    total = 0
    for r in rule:
        total += int(r['amount']) * count_bags_in(r['bag_name']) + int(r['amount'])
    return total

print("Part 1: ", len(count_possible_outer_bags("shiny gold")))
print("Part 2: ", count_bags_in("shiny gold"))