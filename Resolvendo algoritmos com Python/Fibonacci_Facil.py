def fibo(num):
    arr = [0,1]
    if num==1:
        print('0')
    elif num==2:
        print('0 1')
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            fib_list = [  ]
            arr[0]=0
            arr[1]=1
            fib_list.insert(0,'0')
            fib_list.insert(1,'1')
            for i in range(2,num):
                arr[i]=arr[i-1]+arr[i-2]
                fib_list.append(str(arr[i]))
            fib_string = ' '.join(fib_list)
            print(fib_string)
n = int(input())
fibo(n)            