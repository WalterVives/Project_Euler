"""
From: projecteuler.net
Problem ID: 3
Author: Walter Vives
GitHub: https://github.com/WalterVives

Problem:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def larguest_factor(n):
	factor = 0
	for i in range(1,n+1):
		if n == 1:
			break
		if n % i == 0:
			n /= i # n = n/i
			# Save the largest factor
			if i > factor:
				factor = i
	return factor


def main():
	# number
	n = 600851475143
	fact = larguest_factor(n)
	print("The largest factor is: ", fact)


if __name__ == "__main__":
	main()