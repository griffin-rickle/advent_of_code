import util
data = util.get_day_input(6)[0]

counter: int = 0
curr_set = set(data[counter:counter+4])
while len(curr_set) < 4:
    print(curr_set)
    counter += 1
    curr_set = set(data[counter:counter+4])

print(counter + 4)
