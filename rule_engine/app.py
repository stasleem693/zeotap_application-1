
from flask import Flask, request, jsonify, render_template
from ast_utils import create_rule, combine_rules, evaluate_rule, Node, reconstruct_ast

app = Flask(__name__)

# Parse output helper
def parse_output(output):
    return output["message"]

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# API for creating a rule
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    if not rule_string:
        return jsonify({'error': 'Rule string is required'}), 400

    try:
        ast_tree = create_rule(rule_string)
        output = {'message': 'Rule created successfully', 'ast': ast_tree.to_dict()}
        message = parse_output(output)
        return jsonify({'message': message, 'ast': output['ast']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API for combining rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rules = request.json.get('rules')
    if not rules or len(rules) < 2:
        return jsonify({'error': 'At least two rules are required for combination'}), 400

    try:
        combined_ast = combine_rules(rules)
        return jsonify({'message': 'Rules combined successfully', 'ast': combined_ast.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API for evaluating a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    ast_tree = request.json.get('ast')
    data = request.json.get('data')

    if not ast_tree or not data:
        return jsonify({'error': 'AST and data are required'}), 400

    try:
        ast = reconstruct_ast(ast_tree)
        result = evaluate_rule(ast, data)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run Flask application
if __name__ == '__main__':
    app.run(debug=True)

