#include <stdio.h>
#include <math.h>

int main(void) {
	double num1, num2, num3;
	double sum = 0.0;
	double mean, var, std;

	printf("3개의 실수를 입력하시오.: ");
	scanf_s("%lf %lf %lf", &num1, &num2, &num3);

	sum = num1 + num2 + num3;
	mean = sum / 3;

	var = (pow(num1 - mean, 2) + pow(num2 - mean, 2) + pow(num3 - mean, 2)) / 3;
	std = sqrt(var);

	printf("평균: %2f\n", mean);
	printf("표준편차: %2f\n", std);

	return 0;
}