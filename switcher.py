# Function to convert number into string
# Switcher is dictionary data type here
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")

# Driver program
if __name__ == "__main__":
    argument=4
    print (numbers_to_strings(argument))
    dictionary = {
        "a": 1,
        "b": 2
    }
    print(dictionary.get("a"))