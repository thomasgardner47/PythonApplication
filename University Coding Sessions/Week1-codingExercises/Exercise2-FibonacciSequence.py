# The fibonacci Sequence is essentially calculating any number by adding the next two numbers in the sequence
# 0, 1, 1, 2, 3, 5, 8... and so on

def fibonacci(N):  # taking the value
    sequence = [0, 1]
    # N is the number of elements in the sequence we want to find
    # adding 0 and 1 which will produce '1' and adding that 1 into the list
    for n in range(N-2):
        sequence.append(sequence[-1] + sequence[-2])
        # the fibonacci sequence is the sum of the last two elements
        # therefore if element -1 and element -2, im adding the last element into my list together
    return sequence

    seq = fibonacci(10)
    print("First 10 fibonacci number:", seq)
