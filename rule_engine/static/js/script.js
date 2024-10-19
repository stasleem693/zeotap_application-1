document.getElementById('createRuleBtn').addEventListener('click', function() {
    const rule = document.getElementById('rule').value;
    
    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule: rule })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('astOutput').textContent = JSON.stringify(data.ast, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('evaluateRuleBtn').addEventListener('click', function() {
    const ast = document.getElementById('astOutput').textContent;
    const data = document.getElementById('data').value;
    
    fetch('/evaluate_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ast: JSON.parse(ast), data: JSON.parse(data) })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultOutput').textContent = JSON.stringify(data.result, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
