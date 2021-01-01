#one of your homework assignments is to write a method that
#finds twos. It takes two lists and returns any elements that appears in
#both lists containing the digit 2.

#How would we make sure that such a program is working?

def find_twos(first_list, second_list):
    return []

assert(find_twos([], []) == [])
assert(find_twos([2], [12]) == [])
assert(find_twos([12], [12]) == [12])
assert(find_twos([12, 2], [12]) == [12])
assert(find_twos([12, 2, 3], [12, 2]) == [12, 2])
assert(find_twos([12, 3], [12, 2]) == [12])
assert(find_twos([1, 3, 4], [1, 3, 4]) == [])

# Another of your homework problems aks you to write a method that
# takes a comma-separated list of letter ranges and prints
# the individual letters in alphabetical order.

def sort_letters(letter_list):
    pass

assert(sort_letters("b-D,z,m-q,n,C-E")
       == ['B','C','D','E','M','N','O','P','Q','Z'])
