def symmetry(a):
    n = len(a)
    print("The length of n = ", n)
    flag = 0 
    if n%2:
        mid = n // 2 + 1 
    else:
        mid = n // 2
    start1 = 0
    start2 = mid 

    while(start1 < mid and start2 < n):
        if (a[start1]== a[start2]):
            print("a[start1]",a[start1])
            print("a[start2]",a[start2])
            start1 = start1 + 1
            start2 = start2 + 1 
        else:
            flag = 1
            break

    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmeterical")


string = 'lapla'
symmetry(string)
