marks = [12, 2, 3, 4, 4, 54, 455, 5, 56, 6, 7]
index = 0
for index, mark in enumerate(marks):
    print(index, mark)
    if index == 2:
        print("awsome soumya")
    index += 1


fruits = ["apple", "orange", "mango"]
for index, fruit in enumerate(fruits, start = 1):
    print(index, fruit)