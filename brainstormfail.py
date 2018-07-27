import random
import time

topics = ['Animals','Colors','Youtubers','Video Games']
answers = []
timer = 0
t = 0
m = 0

print(f'The chosen topic is {random.choice(topics)}!')


#--------------------------------------------

timer_start = time.time()






print(timer_end)



#---------------------------------------------------



if t == 3:
    for x in range(10):
         single_answer = input('Please enter your answer: ') 
         answers.append(single_answer)
    
for i in answers:
    print(i.center(50,' '))
    timer = 1

t =  timer_start - time.time() 


for w in range(10):
    if t == 59:
        m = m + 1
        t = t - 59



if m == 1 and t == 1:
    print(f'You took {m} minute and {t} second to answer.')
elif m == 0:
    print(f'Wow! Less than a minute! You took only {t} seconds to answer!')
elif  m == 1:
    print(f'You took {m} minute and {t} seconds to answer.')
elif t == 1:
    print(f'You took {m} minutes and {t} second to answer.')
else:
    print(f'You took {m} minutes and {t} seconds to answer.')









#print(f'\n{answers[0]}\n{answers[1]}\n{answers[2]}\n{answers[3]}\n{answers[4]}')
        
        

#print(f'{answers[5]}\n{answers[6]}\n{answers[7]}\n{answers[8]}\n{answers[9]}')




    
    
