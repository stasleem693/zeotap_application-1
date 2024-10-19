class Node:
    def __init__(self, type_, value, left=None, right=None):
        self.type = type_  # 'operator' or 'operand'
        self.value = value  # e.g., 'age > 30' for operand, 'AND' for operator
        self.left = left  # Left child
        self.right = right  # Right child

    def to_dict(self):
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

def create_rule(rule_string):
    if "AND" in rule_string:
        left_cond, right_cond = rule_string.split(" AND ")
        return Node(type_="operator", value="AND",
                    left=Node(type_="operand", value=left_cond.strip()),
                    right=Node(type_="operand", value=right_cond.strip()))
    elif "OR" in rule_string:
        left_cond, right_cond = rule_string.split(" OR ")
        return Node(type_="operator", value="OR",
                    left=Node(type_="operand", value=left_cond.strip()),
                    right=Node(type_="operand", value=right_cond.strip()))
    else:
        raise ValueError("Unsupported rule format")

def combine_rules(rules):
    if len(rules) < 2:
        raise ValueError("At least two rules are required for combination")

    combined_rule = rules[0]
    for rule in rules[1:]:
        combined_rule = Node(type_="operator", value="AND",
                             left=combined_rule,
                             right=create_rule(rule))
    return combined_rule

def evaluate_rule(ast, data):
    if ast.type == 'operand':
        condition = ast.value.split()
        attribute = condition[0]
        operator = condition[1]
        threshold = int(condition[2])

        if operator == '>':
            return data[attribute] > threshold
        elif operator == '<':
            return data[attribute] < threshold
        elif operator == '>=':
            return data[attribute] >= threshold
        elif operator == '<=':
            return data[attribute] <= threshold
        elif operator == '==':
            return data[attribute] == threshold
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    elif ast.type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    return False

def reconstruct_ast(ast_dict):
    if ast_dict is None:
        return None
    node = Node(type_=ast_dict['type'], value=ast_dict['value'])
    node.left = reconstruct_ast(ast_dict.get('left'))
    node.right = reconstruct_ast(ast_dict.get('right'))
    return node

