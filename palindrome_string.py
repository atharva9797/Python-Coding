def palindrome(a):
    d = len(a)
    print("len of a = ", d)
    mid = (len(a)-1)//2
    print ("mid = ",mid)
    start = 0
    last = len(a)-1
    print("last = ",last)
    flag = 0

    while(start <= mid):
        if (a[start] == a[last]):
            start +=1
            last -=1
        else:
            flag = 1
            break;

    if flag == 0:
        print("The entered string is palindrome")
        print("                          ")
        print("==========================")
    else:
        print("The entered string is not palidrome")
        print("                          ")
        print("==========================")

string = "noont"
print("                          ")
print("==========================")
palindrome(string)