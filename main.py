import random
import math

fruits1 = ["apple", 'pineapple', "peach", "pear", "orange", "apricot"]
fruits2 = ["banana", "apple", "orange", "mandarin", "pineapple"]

fruits = [f for f in fruits2 if f in fruits1]
print(fruits)

source_list = [random.randint(-100, 100) for i in range(1,20)]
print(source_list)
new_list = [num for num in source_list if num % 3 == 0 and num > 0 and num % 4 != 0]
print(new_list)
new_list1 = [num if num < 0 else math.sqrt(num) for num in source_list]
print(new_list1)