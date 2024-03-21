#include <stdio.h>

int main(void) {
	long num;
	int cnt = 0;
	int digit;

	printf("정수를 입력하세요.: ");
	scanf_s("%d", &num);

	while (num > 0) {
		digit = num % 10;
		printf("%d ", digit);
		num = num / 10;
	}
	return 0;
}