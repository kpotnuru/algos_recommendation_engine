from data_setup import load_bakery_data
import itertools

baskets, items = load_bakery_data()
item_map = {line[0]: line[1] + " " + line[2] for line in items}

numItems = len(items)
numBaskets = len(baskets)

print(numItems)
print(numBaskets)


# Calculate support for particular item set
def support(item_set):
    basket_subset = baskets
    for it in item_set:
        basket_subset = [basket for basket in basket_subset if it in basket]
    return float(len(basket_subset)) / float(numBaskets)


def apriori_iteration(i, support_items, assoc_rules, new_support_items, min_support, min_confidence):
    for item_set in itertools.combinations(support_items, i):
        item_set = list(item_set)
        if support(item_set) > min_support:
            for j in range(i):
                rule_to = item_set[j]
                rule_from = [x for x in item_set if x != item_set[j]]
                confidence = support(item_set) / support(rule_from)
                if confidence > min_confidence:
                    assoc_rules.append((rule_from, rule_to))
                    for x in item_set:
                        if x not in new_support_items:
                            new_support_items.append(x)
    return assoc_rules, new_support_items


def rule_meta(rule):
    rule_from = [item_map[x] for x in rule[0]]
    return rule_from, item_map[rule[1]]


support_items1 = []
min_support = 0.01
for item in range(numItems):
    item_set = [str(item)]
    if support(item_set) >= min_support:
        support_items1.append(str(item))

min_support = 0.01
min_confidence = 0.5
assoc_rules = []
new_support_items = []

assoc_rules, support_items2 = apriori_iteration(2, support_items1, assoc_rules, new_support_items, min_support,
                                                min_confidence)
assoc_rules, support_items3 = apriori_iteration(3, support_items2, assoc_rules, new_support_items, min_support,
                                                min_confidence)
[rule_meta(rule) for rule in assoc_rules]
