import random
import time


topics = ['Animals','Colors','Youtubers','Video Game','Movies','Books','Tv shows','Foods']
answers = []
timer = 0
t = 0
m = 0


print(f'The chosen topic is {random.choice(topics)}!')


timer_start = time.time()


for x in range(10):
         single_answer = input('Please enter your answer: ') 
         answers.append(single_answer)


print ('You answered'.center(83,'-'))


for i in answers:
    print('|',i.center(79,' '),'|',)  
    print('|',' '.center(79,' '),'|',)  

   


print ('-'.center(83,'-'))


t =  time.time() -  timer_start 


if m == 1 and t == 1:
    print(f'You took {m} minute and {t:.2f} second to answer.'.center(80))
elif m == 0:
    print(f'Wow! Less than a minute! You took only {t:.2f} seconds to answer!'.center(80))
elif  m == 1:
    print(f'You took {m} minute and {t:.2f} seconds to answer.'.center(80))
elif t == 1:
    print(f'You took {m} minutes and {t:.2f} second to answer.'.center(80))
