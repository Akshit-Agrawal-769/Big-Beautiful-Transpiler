KEYWORDS = ['if', 'print', 'while', 'else']
OPERATORS = ['>', '<', '=', '+', '-', '*', '/','>=','<=','==','!=']


def flush(buffer, tokens):
    word = ''.join(buffer)
    if word == '':
        return
    if word in KEYWORDS:
        tokens.append(('keyword', word))
    elif word.isdigit():
        tokens.append(('digit', word))
    else:
        tokens.append(('identifier', word))


def tokenize(code):
    tokens = []
    cumcursor=[]
    for char in code:
        if char==' ':
            flush(cumcursor, tokens)
            cumcursor=[]
        elif char in OPERATORS:
            flush(cumcursor, tokens)
            cumcursor=[]
            tokens.append(('operator',char))
        else:
            cumcursor.append(char)
    flush(cumcursor, tokens) 
    return tokens

code = 'if x>=5 print lol'
print(tokenize(code))