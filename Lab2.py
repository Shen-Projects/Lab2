import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    strlist = x.split(",") # problem is that all values are in str type, need to convert to float
    mylist = [float(i) for i in strlist] # list comprehension: iterates through strlist and converts each string to float and store it in mylist
    print(mylist)
    return mylist

def calc_average(mylist):
    average = sum(mylist) / len(mylist)
    print(average)
    return average

def find_min_max(mylist):
    newlist = [min(mylist), max(mylist)]
    print(newlist)
    return newlist

def sort_temperature(mylist):
    n = len(mylist)
    for i in range(n-1):
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    
    print(mylist)
    return mylist

def calc_median_temperature(mylist):
    median_value = statistics.median(mylist)
    print("Correct median: " + str(median_value))
    return median_value

def calc_median_temperature_two(mylist):
    n = len(mylist)
    m1 = (n - 1) // 2
    m2 = n // 2
    print("string length: " + str(n))
    if n % 2 == 0:
        median_value = (mylist[m1] + (mylist[m2])) / 2
    else:
        median_value = mylist[m2]
    
    print("The median value is " + str(median_value))
    return median_value

if __name__ == "__main__":
    display_main_menu()
    temps = get_user_input()
    calc_average(temps)
    find_min_max(temps)
    sort_temperature(temps)
    calc_median_temperature(temps)
    calc_median_temperature_two(temps)
