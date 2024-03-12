# include <stdio.h>
# define rows 10
# define cols 10

int main(void) {

	int fix[rows][cols] = { 0 };
	int x, y;
	int area = 0;

	for (int i = 0; i < 2; i++) {
		printf("%d번째 사각형: ", i);
		scanf_s("%d %d", &x, &y);

		for (int i = x; i < x + 3; i++) {
			for (int j = y; j < y + 3; j++) {
				fix[i][j] = 1;
			}
		}
	}
	for (int i = 0; i <= 10; i++) {
		for (int j = 0; j <= 10; j++) {
			if (fix[i][j] == 1) {
				area += 1;
			}
		}
	}
	printf("수리해야 하는 타일의 수는 = %d개\n", area);

	return 0;
}