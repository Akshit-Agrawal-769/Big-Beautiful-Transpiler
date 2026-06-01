KEYWORDS = ['if', 'print', 'while', 'else']
OPERATORS = ['>', '<', '=', '+', '-', '*', '/','>=','<=','==','!=']

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
            j=0
            for i in range(len(word)):
                if word[i] in OPERATORS:
                    j=i
                    tokens.append(tokenize(word[:i]))
                    tokens.append(('operator',word[i]))
            if j==0:
                tokens.append(('identifier',word))
            else:
                tokens.append(tokenize(word[j+1:]))

    return tokens

code = 'if x>5 print lol'
print(tokenize(code))