import itertools
def get_value(word,substitution):
    value=0
    factor=1
    for letter in reversed(word):
        value+=substitution[letter]*factor
        factor*=10
    return value
def solve(equation):
    left,right=equation.lower().replace(' ','').split('=')
    left=left.split('+')
    letters=set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters=set(letters)
    digits=range(10)
    for perm in itertools.permutations(digits,len(letters)):
        sol=dict(zip(letters,perm))
        if 0 in [sol[word[0]]for word in left +[right]]:
            continue
        summed=0
        for word in left:
            summed+=get_value(word,sol)
        if summed==get_value(right,sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + f" = {get_value(right, sol)} (mapping: {sol})")
if __name__ == '__main__':
    print('Q1: CROSS + ROADS = DANGER')
    solve('CROSS + ROADS = DANGER')
    print('\nQ2: DONALD + GERALD = ROBERT')
    solve('DONALD + GERALD = ROBERT')
    print('\nQ3: MIT + MANIPAL = MITMAHE')
    solve('MIT + MANIPAL = MITMAHE')
