"""String tokenizer module"""

def tokenize_string(string, modifikators={":"}):
    """Tokenize a string"""
    tokens = []
    
    for i in range(len(string)):
        s = string[i]
        if s in modifikators:
            last_index = len(tokens) - 1
            tokens[last_index] = tokens[last_index] + s
        else:
            tokens.append(s)
    return tokens
        
print(tokenize_string("bo:t"))
