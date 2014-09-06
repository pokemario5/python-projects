import random

print("ask the eight ball")
print("ask a qwestion:")
    
answers = [
       'no',
       'certanly',
       'ha bloop you',
       'you will never meet the girl of your nght',
       ]
while True :
    qwestion = input('>')
    answer = random.choice(answers)      
    print(answer)



