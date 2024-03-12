#include <stdio.h>
#define rows 3
#define cols 3

int main(void) {
	int A[rows][cols] = { {2, 3, 0}, {8, 9, 1}, {7, 0, 1} };
	int B[rows][cols] = { {1, 0, 0}, {0, 1, 0}, {0, 0, 1} };
	int C[rows][cols];

	for (int r = 0; r < rows; r++) {
		for (int c = 0; c < cols; c++) {
			C[r][c] = A[r][c] + B[r][c];
			printf("%d ", C[r][c]);
		}
		printf("\n");
	}
	return 0;
}