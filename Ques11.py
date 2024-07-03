str = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for i in str:
    if i in vowels:
        count += 1
print("Total number of vowels:", count)