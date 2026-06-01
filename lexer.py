KEYWORDS = ['if', 'print', 'while', 'else']
OPERATORS = ['>', '<', '=', '+', '-', '*', '/']

def tokenize(code):
    tokens = []
    for word in code.split():
        if word.isdigit():
            tokens.append(('digit',word))
        if word in KEYWORDS:
            tokens.append(('keyword',word))
        if word in OPERATORS:
            tokens.append(('operator',word))
        else:
            tokens.append(('identifier',word))
    return tokens