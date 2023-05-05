
import state
import frontier
import time

def search(n):
    s=state.create(n) #state + a symbol
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return s
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0


num_ave = 0
num_of_plays = 100
n_puzzle = 3
for i in range(num_of_plays):
    start_time = time.time()
    search(n_puzzle)
    end_time = time.time()
    if (end_time - start_time) >30 :
        print(f'{n_puzzle}*{n_puzzle} puzzle time out')
        raise TimeoutError
    num_ave += end_time - start_time

print(f'Average time of {num_of_plays} plays for {n_puzzle}*{n_puzzle} puzzle is: ', num_ave / num_of_plays)



#one time run:
'''
length = 1
start_time = time.time()
print(search(length ))
end_time = time.time()
print("search", length, "running time", end_time-start_time)
'''