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
rev_pairs = dict(zip(openers, closers))
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
repair_score = {')': 1, ']': 2, '}': 3, '>': 4}

e_score = 0
r_scores = []

for line in raw_inp.splitlines():
    print('start scan')
    stack = []
    corrupted = False
    for char in line:
        if char in openers:
            stack.append(char)
            # print('char: ', char)
        elif char in closers:
            popped = stack.pop()
            # print('char:', char, 'pop:', popped)
            if popped != pairs[char]:
                print('corrupted')
                corrupted = True
                e_score += error_score[char] # we found our first mismatch
                break
    print('end scan')

    if len(stack) > 0 and not corrupted:
        # we have unclosed symbols, incomplete line
        # go through stack in reverse and create a string of the correct characters
        repair = []
        r_score = 0
        for char in stack[::-1]:
            # print(char)
            repair.append(rev_pairs[char])
            r_score *= 5
            r_score += repair_score[repair[-1]]
        r_scores.append(r_score)
        
        # print('incomplete')
        # print("".join(repair))
r_score_final = sorted(r_scores)[len(r_scores)//2]

print('e score:', e_score)
print('r score:', r_score_final)      
