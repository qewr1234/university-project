#include <stdio.h>
#include <math.h>

int main(void) {
	double num1, num2, num3;
	double sum = 0.0;
	double mean, var, std;

	printf("3���� �Ǽ��� �Է��Ͻÿ�.: ");
	scanf_s("%lf %lf %lf", &num1, &num2, &num3);

	sum = num1 + num2 + num3;
	mean = sum / 3;

	var = (pow(num1 - mean, 2) + pow(num2 - mean, 2) + pow(num3 - mean, 2)) / 3;
	std = sqrt(var);

	printf("���: %2f\n", mean);
	printf("ǥ������: %2f\n", std);

	return 0;
}