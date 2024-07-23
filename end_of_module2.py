def result(num):
    result_ = ""
    dels = []
    for i in range(3, num+1):
        if num % i == 0:
            dels.append(i)

    i = 1
    flag = True
    while flag:
        for del_ in dels:
            if i <= int(del_ / 2):
                str_ = str(i) + str(del_-i)
                if i != del_-i:
                    result_ += str_
            elif i > int(dels[len(dels)-1]/2):
                flag = False
        if len(dels) > 0:
            i += 1
        else:
            break

    return result_


num = 0
while True:
    num = int(input("Enter number: "))
    if num >= 3 and num <= 20:
        print(result(num))
