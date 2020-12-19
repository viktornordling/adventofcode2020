class Rule:

    def __init__(self, rule_id):
        self.rule_id = rule_id

    def matches(self, str, rule_dict):
        return []


class SerialRule(Rule):
    rules = []

    def __init__(self, rules, rule_id):
        super().__init__(rule_id)
        self.rules = rules

    def eval_serial_recursive(self, str, sub_rules, rule_dict):
        if len(sub_rules) == 0:
            return [str]
        cur: Rule = sub_rules[0]
        sub_matches = cur.matches(str, rule_dict)
        all_results = []
        for match in sub_matches:
            gg = self.eval_serial_recursive(match, sub_rules[1:], rule_dict)
            all_results += gg
        return all_results

    def matches(self, str, rule_dict):
        return self.eval_serial_recursive(str, self.rules, rule_dict)


class OrRule(Rule):
    rules = []

    def __init__(self, rules, rule_id):
        super().__init__(rule_id)
        self.rules = rules

    def matches(self, str, rule_dict):
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
        if len(str) > 0 and str[0] == self.literal:
            return [str[1:]]
        return []


class RuleRef(Rule):
    rid = None

    def __init__(self, rid):
        super().__init__(rid)
        self.rid = rid

    def matches(self, str, rule_dict):
        rule = rule_dict[self.rid]
        return rule.matches(str, rule_dict)


rules_being_built = set()


def parse_or_get_rule(line_map, rule_dict, rule_str="", line_id=""):
    if rule_str != "":
        rule = rule_str.strip()
    else:
        rule = line_map[int(line_id)]

    rparts = [p.strip() for p in rule.split(":")]
    rid = int(rparts[0])
    if rid in rule_dict:
        return rule_dict[rid]
    elif rid in rules_being_built:
        return RuleRef(rid)
    rules_being_built.add(rid)
    body: str = rparts[1].strip()
    if "|" in body:
        or_rule_parts = body.split("|")
        left = or_rule_parts[0].strip().split(" ")
        right = or_rule_parts[1].strip().split(" ")
        left_rule = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id.strip()) for line_id in left], "{}_l".format(rid))
        right_rule = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id.strip()) for line_id in right], "{}_r".format(rid))
        rule_dict[rid] = OrRule([left_rule, right_rule], rid)
    elif body.startswith("\""):
        literal = body.replace("\"", "")
        rule_dict[rid] = LiteralRule(literal, rid)
    else:
        rule_dict[rid] = SerialRule([parse_or_get_rule(line_map, rule_dict, line_id=line_id) for line_id in body.split(" ")], rid)
    rules_being_built.remove(rid)
    return rule_dict[rid]


def check(regex, str, rule_dict):
    m = regex.matches(str, rule_dict)
    return len(m) > 0 and m[0] == ""


def count_valid_strings(data):
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
        parse_or_get_rule(line_map, rule_dict, rule_str=rule.strip())

    rule0: Rule = rule_dict[0]
    return len([str for str in string_part.split("\n") if check(rule0, str, rule_dict)])


def solve():
    print("Part 1:", count_valid_strings(open('input.txt', 'r').read()))
    print("Part 2:", count_valid_strings(open('input2.txt', 'r').read()))



solve()
