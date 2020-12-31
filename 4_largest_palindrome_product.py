"""
From: projecteuler.net
Problem ID: 4
Author: Walter Vives
GitHub: https://github.com/WalterVives

Problem:

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
part1 = []
part2 = []
result = 0
for i in range(100,1000):
	for j in range(100,1000):
		multiplication = i * j
		multiplication = list(str(multiplication))
		if len(multiplication) == 6:
			part1 = multiplication[0], multiplication[1], multiplication[2]
			part2 = multiplication[3], multiplication[4], multiplication[5]
			# Palindrome
			if part1[::-1] == part2:
				# List of numbers to int number
				num = int("".join(multiplication))
				# Add the largest palindrome product
				if num > result:
					# result
					result = num
					# Number 1
					x = i
					# Number 2
					y = j
					#print(i, "*", j, "=", result)
print(x, "*", y, "=", result)