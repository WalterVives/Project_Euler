/*
From: projecteuler.net
Problem ID: 5
Author: Walter Vives
GitHub: https://github.com/WalterVives

Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include<iostream>

using namespace std;

int multiples(int x, int y){
	
	int total_sum = 0;

	for(int i=0;i<1000;i++){
		if(i % x == 0 || i % y == 0)
		{
			total_sum += i;

		}
	}
	return total_sum;

}

int main(){

	cout << "The answer is: " << multiples(3,5) << endl;

	return 0;

}