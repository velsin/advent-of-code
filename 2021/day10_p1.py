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


e_score = 0

# print(pairs)

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
                e_score += error_score[char] # we found our first mismatch
                break
    print('end scan')

    if len(stack) > 0:
        # we have unclosed symbols, incomplete line
        print('incomplete')
        

print(e_score)      
