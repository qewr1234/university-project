#include <stdio.h>
#define KMH_TO_MS (1000/3600.0)

int main(void) {
	float distance = 18.4;
	float speed = 160 * KMH_TO_MS;
	float time = distance / speed;

	printf("���ӱ��� Ȩ�÷���Ʈ�� �����ϴ� �� �ɸ��� �ð�: %f��\n", time);

	return 0;
}