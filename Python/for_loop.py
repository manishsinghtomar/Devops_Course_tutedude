a = [1,2,3,4,5]

for i in a:
    print(i)
    if i == 3:
       print("index 3 element is printed ")

numbers = list(range(10))
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    if i == 1:
        print('ONE')
    elif i == 2:
        print('TWO')
    elif i == 3:
        print('THREE')
    else:
        print("other")