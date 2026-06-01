def parse(tokens):
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == ('keyword', 'if'):
            i = parse_if(tokens, i)
        i += 1

def parse_if(tokens, i):
    pass