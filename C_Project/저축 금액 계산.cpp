#include <stdio.h>

int main(void) {
	int money = 0;
	int day = 0;
	int bus = 0;
	int food = 0;
	int pockmoney = 0;
	int total = 0;

	printf("������ �Է��Ͻÿ�.: ");
	scanf_s("%d", &money);

	printf("�� �޿� ��ĥ�̳� ����ϳ���.: ");
	scanf_s("%d", &day);

	printf("�Ϸ� ����� �Է��Ͻÿ�.: ");
	scanf_s("%d", &bus);

	printf("�Ϸ� �ĺ� �Է��Ͻÿ�.: ");
	scanf_s("%d", &food);

	printf("�Ϸ� �뵷�� �Է��Ͻÿ�.: ");
	scanf_s("%d", &pockmoney);

	total = money - (bus + food + pockmoney) * day;

	printf("�������: %d", total);

}