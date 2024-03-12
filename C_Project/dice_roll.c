#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 6

int main(void) {
	int dice[SIZE] = { 0 };

	srand(time(NULL));

	for (int i = 0; i < 100; i++) {
		int result = rand() % SIZE; // �ֻ��� �� ����
		dice[result]++; // �ֻ��� ���� ���� ������ �ش� �迭 ��Ҹ� ������Ŵ

	}
	for (int i = 0; i < SIZE; i++) {
		printf("%d: %d��\n", i + 1, dice[i]);
	}
	return 0;
}