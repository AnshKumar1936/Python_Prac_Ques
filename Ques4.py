def fibonacci(n):
    list= [0, 1]
    for i in range(2, n):
        list.append(list[i-1] + list[i-2])
    return list


number = int(input("Enter the number: "))
fib = fibonacci(number)
print("Fibonacci Series:", fib)