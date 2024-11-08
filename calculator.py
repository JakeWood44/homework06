from pair import *

def tokenize(expression):
    expression = expression.replace("(", "( ")
    expression = expression.replace(")", " )")

    return expression.split()

def parse_tokens(tokens, i):
    if tokens[i] == "(":
        op = tokens[i + 1]

        if i != 0:
            new_tokens = parse_tokens(tokens, i + 2)[0]
            i = parse_tokens(tokens, i + 2)[1]

            op = Pair(op, new_tokens)

        else:
            i += 2

        recurse = parse_tokens(tokens, i)
        i = recurse[1]

        return Pair(op, recurse[0]), i

    elif tokens[i] == ")":
        return nil, i + 1

    else:
        try:
            if "." in tokens[i]:
                num = float(tokens[i])
            else:
                num = int(tokens[i])

            new_pairs, i = parse_tokens(tokens, i + 1)
            return Pair(num, new_pairs), i

        except:
            raise TypeError("wrong type")
