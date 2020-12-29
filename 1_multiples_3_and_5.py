"""
Find the sum of all multiples of 3 and 5 below 1,000.
"""
# Numbers.
x = 3
y = 5
# Total sum
total_sum = 0

for i in range(1,1000):
	if i % x  == 0 or i % y == 0:
		total_sum += i

print(total_sum)