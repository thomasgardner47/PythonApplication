def bubble(L):  # The 'def' keyword is used to define the function
    N = len(L)  # inside the function

    for i in range(N):  # 'i' being the loop counter and 'range' being able to loop upto a number, there whatever number
        for j in range(N):  # the second for loop performs in the same way as the first but with 'j' as the lopp counter
            if L[i] < L[j]:  # if list i is less than list j, then swap them around
                L[i], L[j] = L[j], L[i]


L = [1, 5, 3, 2, 4, 6]

print(L)
bubble(L)
print("Sorted List:", L)
