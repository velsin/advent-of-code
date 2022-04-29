TEST = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

with open('./data/day10.txt') as f:
    raw_inp = f.read()

# raw_inp = TEST

# use a stack and dictionary approach, go line by line
openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
pairs = dict(zip(closers, openers))
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}


score = 0

print(pairs)

for line in raw_inp.splitlines():
    print('start scan')
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
            # print('char: ', char)
        elif char in closers:
            popped = stack.pop()
            # print('char:', char, 'pop:', popped)
            if popped != pairs[char]:
                print('mismatch')
                score += error_score[char] # we found our first mismatch
                break
    print('end scan')

    if len(stack) > 0:
        # we have unclosed symbols, incomplete line
        print('incomplete')
        

print(score)      



def isValid(s: str) -> bool:
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"]
    pairs = dict(zip(closers, openers))
    stack = []

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in closers:
            try:
                if stack.pop() != pairs[char]:
                    return False
            except IndexError:  # popping from empty stack
                return False

    if len(stack) > 0:
        return False  # unclosed parentheses

    return True
