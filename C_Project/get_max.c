#include <stdio.h>

int get_integer() {
	int value;
	printf("������ �Է��Ͻÿ�.: ");
	scanf_s("%d", &value);
	return value;
}

int get_max(int x, int y) {
	if (x > y)
		return x;
	else
		return y;
}

int main(void) {
	int a = get_integer();
	int b = get_integer();

	printf("�� �� �߿��� ū ���� %d�Դϴ�. \n", get_max(a, b));

	return 0;
}