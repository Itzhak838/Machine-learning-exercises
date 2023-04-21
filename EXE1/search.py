import state
import frontier


def search(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    f = frontier.create(state.create(n))
    check_times = 0
    while not frontier.is_empty(f):
        check_times += 1
        s = frontier.remove(f)
        if state.is_target(s):
            return s, check_times
        ns = state.get_next(s)
        for j in ns:
            frontier.insert(f, j)
    return 0


# play = search(4)
# print(play, "\n", len(play[1]), "steps")
depth_ave = 0
num_ave = 0
num_of_plays = 1
n_puzzle = 4
for i in range(num_of_plays):
    play = search(n_puzzle)
    num_ave += play[1]
    depth_ave += len(play[0][1])
print("Average number", num_ave / num_of_plays, "\nAverage depth", depth_ave / num_of_plays)

"""
Search(2):
Average number 6.76 
Average depth 1.58
Search(3):
Average number 995.27 
Average depth 5.7
Search(4): *run 1 time - 100 is too big for my computer
Average number 5541873.0 
Average depth 19.0
Conclusion:
As the length of the puzzle increases, 
the number of runs increases and we will
 need more memory and computing power.
"""
