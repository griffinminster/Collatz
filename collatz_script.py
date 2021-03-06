import locale
import sys

import plotly.express as px
from tqdm import tqdm


def main():
    #Determines whether to split numbers with commas or periods
    locale.setlocale(locale.LC_ALL, '')

    options = ""
    while options != 'r' or options != 'n':
        options = input("Would you like to test a range or one number? (r/n): ")
        if options == 'r':
            range_option()
        elif options == 'n':
            number_option()
    


def range_option():
    #Parse inputs
    num_range = -1
    while num_range <= 0:
        num_range = int(input("What number do you want to test up to? "))
    input_arr = list(range(1, num_range+1))

    overall_max = (-1, -1)
    overall_tst = (-1, -1)

    max_x = []
    max_y = []
    most_x = []
    most_y = []

    #Main loop, going through each number, adds progress bar with tqdm
    for elem in tqdm(input_arr):
        num = elem
        highest = elem
        counter = 0
        curr_x = [counter]
        curr_y = [num]

        #Performs main 3n+1 or n/2 computation until 1 is reached, ending the loop
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = num * 3 + 1
            highest = max(num, highest)
            counter += 1
            
            curr_x.append(counter)
            curr_y.append(num)

        #Prints results for each number, only if inital number was 100 or less
        if num_range <= 100:
            print_each_result(elem, highest, counter)

        #Figure out overall results for max number reached and most numbers gone through each loop pass
        if highest >= overall_max[1]:
            overall_max = (elem, highest)
            max_x = array_copy(curr_x, curr_y, max_x, max_y)[0]
            max_y = array_copy(curr_x, curr_y, max_x, max_y)[1]
        
        if counter >= overall_tst[1]:
            overall_tst = (elem, counter+1)
            most_x = array_copy(curr_x, curr_y, most_x, most_y)[0]
            most_y = array_copy(curr_x, curr_y, most_x, most_y)[1]
            
        curr_x.clear()
        curr_y.clear()

    #Print overall highest number reached and most numbers stepped through
    print("\n\nOVERALL RESULTS")
    print(f"Highest Number Reached: {overall_max[1]:n} from #{overall_max[0]:n}")
    print(f"Largest Total Stopping Time: {overall_tst[1]:n} from #{overall_tst[0]:n}")


    fig1 = px.line(x = max_x, y = max_y, 
                    title = "Highest Number Reached: From " + str(overall_max[0]), 
                    labels={'x':"Number Hit", 'y':"Result of Computation"})
    fig2 = px.line(x = most_x, y = most_y, 
                    title = "Largest Total Stopping Time: From " + str(overall_tst[0]), 
                    labels={'x':"Numbers Hit", 'y':"Result of Computation"})
    fig1.show()
    fig2.show()
    
    sys.exit()
    
    
def number_option():
    num = -1
    while num <= 0:
        num = int(input("What number do you want to test? "))
    starter = num
    highest = num
    counter = 0
    max_x = [counter]
    max_y = [num]
    
    #Performs main 3n+1 or n/2 computation until 1 is reached, ending the loop
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        highest = max(num, highest)
        counter += 1
        
        max_x.append(counter)
        max_y.append(num)
    
    #Prints results
    print_each_result(starter, highest, counter)
    
    fig3 = px.line(x = max_x, y = max_y, 
                    title = "Number: " + str(starter), 
                    labels={'x':"Numbers Hit", 'y':"Result of Computation"})
    fig3.show()
    
    sys.exit()
    
    
def print_each_result(number, highest, counter):
    print(f"Starting Number: {number}")
    print(f"Highest peak: {highest}")
    print(f"Numbers gone through: {counter+1}")
    print()

def array_copy(curr_x, curr_y, list_x, list_y):
    list_x.clear()
    list_y.clear()
    list_x = curr_x[:]
    list_y = curr_y[:]
    return (list_x, list_y)


if __name__ == "__main__":
    main()
