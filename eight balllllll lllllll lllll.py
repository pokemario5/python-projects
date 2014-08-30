import random
print('ask the 8-ball:')
question = input('> ')

answers = [
    'yes',
    'no',
    'aswome',
    'noooooooooooo',
    'shore',
    'know idea dude',
    'who that',
    'iam your wishing ball so yes',
    'what in the name skip stap',
    'whats up   dudeeeeeeeeee',
    'OOOOOOOOOOOOOOOOOOOOOOOHHHHHHHHHHHHHH',
    'hello zambie',
    'supercalafragilistispyallodoshins'
 ]   
while True:
    print('ask the 8-ball:')
    question = input('> ')
    answer = random.choice(answers)
    print(answer)
    print()                 
