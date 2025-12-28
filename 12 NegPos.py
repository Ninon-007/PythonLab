# Input 4 integers (+ve and −ve). Write a Python code to find the sum of
# negative numbers, positive numbers, and print them. Also, find the
# averages of these two groups of numbers and print.

pos_sum = 0
neg_sum = 0
pos_count = 0
neg_count = 0
for i in range(4):
    num = int(input(f"Enter {i+1}th number: "))
    if num > 0:
        pos_sum += num
        pos_count += 1
    else:
        neg_sum += num
        neg_count += 1
print(f"Sum of positive numbers: {pos_sum}")
print(f"Sum of negative numbers: {neg_sum}")
print(f"Average of positive numbers: {pos_sum/pos_count}")
print(f"Average of negative numbers: {neg_sum/neg_count}")