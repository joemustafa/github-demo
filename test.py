import time

print("I am hungry")
print("What to eat")
print("That sounds good")
def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        print("Entering {0}" + some_function )
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function())
