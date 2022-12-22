import util

needed_consecutive_chars = 4
data = util.get_day_input(6)[0]

counter: int = 0
curr_set = set(data[counter:counter + needed_consecutive_chars])
while len(curr_set) < needed_consecutive_chars:
    counter += 1
    curr_set = set(data[counter:counter + needed_consecutive_chars])

print(counter + needed_consecutive_chars)
