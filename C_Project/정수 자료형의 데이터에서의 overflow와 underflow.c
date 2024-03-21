#include <stdio.h>

int main(void) {
	printf("INT_MAX = %d = 0X%X\n", 2147483647, 2147483647);
	printf("INT_MAX + 1 = %d = 0X%X\n", 2147483647 + 1, 2147483647 + 1);
	printf("INT_MIN = %d = 0X%X\n", -2147483648, -21474836478);
	printf("INT_MIN = %d = 0X%X\n", -2147483648 - 1, -2147483648 - 1);
}