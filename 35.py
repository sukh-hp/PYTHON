# Rock Paper Scissor


import random
list1 = ['Rock', 'Paper', 'Scissor']
dic1 = {'R':'Rock', 'P':'Paper', 'S':'Scissor'}
print('         Welcome To the Rock , Paper , Scissor Game !\n                Select One of the Below\n                     R for Rock\n                     P for Paper\n                     S for Scissor')

com_wins = 0
you_wins = 0
com_points = 0
you_points = 0

def wins():
    if com_wins==0 and you_wins ==0:
        None
    else:
        print(f'            Computer Wins ={com_wins} ')
        print(f'              Your Wins ={you_wins} ')
# print(wins())
# 
while com_points!=5 or you_points!=5:     
    while True:
        a = input('              What is Your Choice--->')
        if a.upper() == 'R':
            break
        elif a.upper() == 'S':
            break
        elif a.upper() == 'P':
            break
        else:
            print('Please Check Your Inputs')
            continue
    b = random.choices(list1)
    
    if b[0] == 'Rock' and dic1[a.upper()]=='Paper':
        you_points+=1
    if b[0] == 'Rock' and dic1[a.upper()]=='Scissor':
        com_points+=1
    if b[0] == 'Rock' and dic1[a.upper()]=='Rock':
        None
    if b[0] == 'Paper' and dic1[a.upper()]=='Paper':
        None
    if b[0] == 'Paper' and dic1[a.upper()]=='Scissor':
        you_points+=1
    if b[0] == 'Paper' and dic1[a.upper()]=='Rock':
        com_points+=1
    if b[0] == 'Scissor' and dic1[a.upper()]=='Paper':
        com_points+=1
    if b[0] == 'Scissor' and dic1[a.upper()]=='Scissor':
        None
    if b[0] == 'Scissor' and dic1[a.upper()]=='Rock':
        you_points+=1
    
    print('Computer choice              Your Choice             Points')
    print(f'{b[0]}                      {dic1[a.upper()]}                      {com_points}-{you_points}')
    while com_points==5 or you_points==5:
        if you_points>com_points:
            print('                      Congratulations !')
            you_wins+=1
        else:
            print('                    Sorry !')
            com_wins+=1
        com_points = 0
        you_points = 0
        wins()
        again_check = input('     Do You Want To Play One More Time? Y or N--->')
    if com_points!=5 or you_points!=5:
        continue
    else:
        again_check = input('     Do You Want To Play One More Time? Y or N--->')
        if again_check.upper()=='Y':
            continue
        break