#include <stdio.h>

int main(void) {
	int money = 0;
	int day = 0;
	int bus = 0;
	int food = 0;
	int pockmoney = 0;
	int total = 0;

	printf("월급을 입력하시오.: ");
	scanf_s("%d", &money);

	printf("한 달에 며칠이나 출근하나요.: ");
	scanf_s("%d", &day);

	printf("하루 교통비를 입력하시오.: ");
	scanf_s("%d", &bus);

	printf("하루 식비를 입력하시오.: ");
	scanf_s("%d", &food);

	printf("하루 용돈을 입력하시오.: ");
	scanf_s("%d", &pockmoney);

	total = money - (bus + food + pockmoney) * day;

	printf("저축액은: %d", total);

}