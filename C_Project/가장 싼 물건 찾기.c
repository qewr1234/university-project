#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

int main(void) {
	int prices[SIZE] = { 0 };
	int min = 0;

	printf("------------------------------\n");
	printf("1  2  3  4  5  6  7  8  9  10\n");
	printf("------------------------------\n");
	srand((unsigned)time(NULL));

	for (int i = 0; i < SIZE; i++) {
		prices[i] = (rand() % 100) + 1;
		printf("%-3d", prices[i]); // %-3d�� 3�ڸ��� �ʵ忡 ���� �����Ͽ� ���
	}
	printf("\n\n");
	for (int k = 0; k < SIZE; k++){
		for (int i = 0; i < SIZE - k - 1; i++) {
			if (prices[i] > prices[i + 1]) {
				int temp = prices[i]; prices[i] = prices[i + 1]; prices[i + 1] = temp;
			}
		}
		min = prices[0];
	}
	for (int i = 0; i < SIZE; i++) {
		printf("%d, ", prices[i]);
	}
	printf("\n");
	printf("���� �� ������: %d�Դϴ�.\n", min);

	return 0;
}