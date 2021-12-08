import locale
from tqdm import tqdm

locale.setlocale(locale.LC_ALL, '')

num_range = int(input("What number do you want to test up to? "))
input_arr = [x for x in range(1, num_range+1)]

overall_max = (-1, -1)
overall_most = (-1, -1)

for elem in tqdm(input_arr):
    num = elem
    highest = elem
    counter = 0

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        highest = max(num, highest)
        counter += 1

    # print(f"Starting Number: {elem}")
    # print(f"Highest peak: {highest}")
    # print(f"Numbers gone through: {counter+1}")
    # print()

    if highest >= overall_max[1]:
        overall_max = (elem, highest)
    if counter >= overall_most[1]:
        overall_most = (elem, counter+1)

print("\n\nOVERALL RESULTS")
print(f"Highest Number Reached: {overall_max[1]:n} from #{overall_max[0]:n}")
print(f"Most Numbers Hit: {overall_most[1]:n} from #{overall_most[0]:n}")
