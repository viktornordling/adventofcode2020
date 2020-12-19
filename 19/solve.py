class Rule:

    def __init__(self, rule_id):
        self.rule_id = rule_id

    def matches(self, str, rule_dict):
        return True


class SerialRule(Rule):
    rules = []

    def __init__(self, rules, rule_id):
        super().__init__(rule_id)
        self.rules = rules

    def matches(self, str, rule_dict):
        print("Evaluating serial rule", self.rule_id)
        rest_queue = [str]
        rests_for_next_rule = []
        matches = []
        for rule in self.rules:
            rule_has_matches = False
            rest_queue += rests_for_next_rule
            rests_for_next_rule = []
            while len(rest_queue) > 0:
                rest = rest_queue.pop(0)
                matches = rule.matches(rest, rule_dict)
                if len(matches) == 0:
                    # No matches.
                    print("no matches")
                elif len(matches) == 1:
                    rests_for_next_rule.append(matches[0])
                    rule_has_matches = True
                else:
                    rule_has_matches = True
                    for r in matches:
                        rests_for_next_rule.append(r)
            if not rule_has_matches:
                return []
        return matches


class OrRule(Rule):
    rules = []

    def __init__(self, rules, rule_id):
        super().__init__(rule_id)
        self.rules = rules

    def matches(self, str, rule_dict):
        print("Evaluating or rule", self.rule_id)
        rest_list = []
        for rule in self.rules:
            matches = rule.matches(str, rule_dict)
            if len(matches) > 0:
                rest_list += matches
        return rest_list


class LiteralRule(Rule):
    literal = ''

    def __init__(self, literal, rule_id):
        super().__init__(rule_id)
        self.literal = literal

    def matches(self, str, rule_dict):
        print("Evaluating literal rule", self.rule_id)
        if len(str) > 0 and str[0] == self.literal:
            return [str[1:]]
        return []


class RuleRef(Rule):
    rid = None

    def __init__(self, rid):
        super().__init__(rid)
        self.rid = rid

    def matches(self, str, rule_dict):
        print("Evaluating rule ref", self.rule_id)
        rule = rule_dict[self.rid]
        return rule.matches(str, rule_dict)


rules_being_built = set()


def parse_or_get_rule(line_map, rule_dict, rule_str="", line_id=""):
    # print("rule_str = ", rule_str)
    # print("line_id = ", line_id)
    if rule_str != "":
        rule = rule_str.strip()
    else:
        rule = line_map[int(line_id)]

    rparts = [p.strip() for p in rule.split(":")]
    rid = int(rparts[0])
    if rid in rule_dict:
        return rule_dict[rid]
    elif rid in rules_being_built:
        # print("rid {} in rules_being_built, returning a RuleRef".format(rid, rules_being_built))
        return RuleRef(rid)
    rules_being_built.add(rid)
    body: str = rparts[1].strip()
    if "|" in body:
        # print("parsing or rule")
        or_rule_parts = body.split("|")
        left = or_rule_parts[0].strip().split(" ")
        right = or_rule_parts[1].strip().split(" ")
        left_rule = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id.strip()) for line_id in left], "{}_l".format(rid))
        right_rule = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id.strip()) for line_id in right], "{}_r".format(rid))
        rule_dict[rid] = OrRule([left_rule, right_rule], rid)
    elif body.startswith("\""):
        # print("parsing literal rule")
        literal = body.replace("\"", "")
        rule_dict[rid] = LiteralRule(literal, rid)
    else:
        # print("parsing serial rule")
        rule_dict[rid] = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id) for line_id in body.split(" ")], rid)
    rules_being_built.remove(rid)
    return rule_dict[rid]


def check(regex, str, rule_dict):
    m = regex.matches(str, rule_dict)
    return len(m) > 0 and m[0] == ""


def solve_part_1(data):
    parts = data.split("\n\n")
    rule_part = parts[0]
    string_part = parts[1]

    rules = rule_part.split("\n")

    rule_dict = {}
    line_map = {}
    for rule in rules:
        rparts = rule.split(":")
        rid = int(rparts[0])
        line_map[rid] = rule

    for rule in rules:
        # print("parsing line:", rule)
        parse_or_get_rule(line_map, rule_dict, rule_str=rule.strip())

    rule0: Rule = rule_dict[0]
    count = 0
    for str in string_part.split("\n"):
        print("Testing line:", str)
        if check(rule0, str, rule_dict):
            print("Valid")
            count += 1
        else:
            print("Invalid")

    return count


def solve():
    # data2 = open('easy.txt', 'r').read()
    # data = open('input.txt', 'r').read()
    # data2 = open('easy2_noloop.txt', 'r').read()
    data2 = open('debug.txt', 'r').read()
    print("Part 2:", solve_part_1(data2))
    # print("*************************")
    # print("*************************")
    # print("*************************")
    # data2 = open('easy2_loop.txt', 'r').read()
    # print("Part 2:", solve_part_1(data2))
    # data2 = open('input2.txt', 'r').read()

    # print("Part 1:", solve_part_1(data))



solve()
