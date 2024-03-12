#include <stdio.h>
#define KMH_TO_MS (1000/3600.0)

int main(void) {
	float distance = 18.4;
	float speed = 160 * KMH_TO_MS;
	float time = distance / speed;

	printf("강속구가 홈플레이트에 도달하는 데 걸리는 시간: %f초\n", time);

	return 0;
}