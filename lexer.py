KEYWORDS = ['if', 'print', 'while', 'else']
OPERATORS = ['>', '<', '=', '+', '-', '*', '/','>=','<=','==','!=']
PUNCTUATION = [':']

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
    i=0
    while i <len(code):
        if code[i]==' ':
            flush(cumcursor, tokens)
            cumcursor=[]
        elif code[i] in OPERATORS:
            flush(cumcursor, tokens)
            cumcursor=[]
            if code[i+1] in OPERATORS:
                tokens.append(('operator',code[i]+code[i+1]))
                i+=1
            else:
                tokens.append(('operator',code[i]))
        else:
            cumcursor.append(code[i])
        i+=1

    flush(cumcursor, tokens) 
    return tokens

code = 'if x>=5 print lol'
print(tokenize(code))