#include <stdio.h>
#include <stdlib.h>

int main(void) {
	double* pArray;
	int size, i;

	printf("input size: ");
	scanf_s("%d", &size);
	pArray = (double*)calloc(size, sizeof(double));
	
	if (pArray == NULL) {
		printf("동적 배열 생성 오류\n");
		exit(1);
	}
	for (int i = 0; i < size; i++)
		pArray[i] = 0.0;
	free(pArray);
	return 0;
}
