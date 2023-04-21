def process(s):
    should_add = True
    result = []
    for c in s:
        if c != '(' and c != ')' and should_add:
            result.append(c)
        if c == '(':
            should_add = False
        if c == ')':
            should_add = True

    return "".join(result)

if __name__ == "__main__":
    s = input()
    print(process(s))