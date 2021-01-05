/*
From: projecteuler.net
Problem ID: 3
Author: Walter Vives
GitHub: https://github.com/WalterVives

Problem:

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
#include <iostream>

using namespace std;

int largest_factor(long int n){
	int factor = 0;
	for(int i=1;n+1;i++){
		if(n == 1)
		{
			break;
		}
		if(n%i == 0)
		{
			n /= i; // n = n/i;
		}
		if(i>factor)
		{
			factor=i;
		}

	}
	return factor;
}

int main(){

	long int n = 600851475143;
	cout << "The largest factor is: " << largest_factor(n) << endl;


	return 0;
}