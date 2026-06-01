KEYWORDS = ['if', 'print', 'while', 'else']
OPERATORS = ['>', '<', '=', '+', '-', '*', '/']

def tokenize(code):
    tokens = []
    for word in code.split():
        if word.isdigit():
            tokens.append(('digit',word))
        elif word in KEYWORDS:
            tokens.append(('keyword',word))
        elif word in OPERATORS:
            tokens.append(('operator',word))
        else:
            tokens.append(('identifier',word))
    return tokens

code = 'if x > 5 print lol'
print(tokenize(code))