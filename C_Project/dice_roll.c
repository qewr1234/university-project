#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 6

int main(void) {
	int dice[SIZE] = { 0 };

	srand(time(NULL));

	for (int i = 0; i < 100; i++) {
		int result = rand() % SIZE; // 주사위 값 생성
		dice[result]++; // 주사위 값이 나올 때마다 해당 배열 요소를 증가시킴

	}
	for (int i = 0; i < SIZE; i++) {
		printf("%d: %d번\n", i + 1, dice[i]);
	}
	return 0;
}