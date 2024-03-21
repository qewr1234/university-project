#include <stdio.h>
#include <stdlib.h>
#define LINE_SIZE 10
void genBigRandArray(int* array, int size);
void printArraySample(int* array, int size, int line_size);

void main() {
	int* array;

	for (int size = 200000; size <= 1000000; size += 200000) {
		printf("Testing generation of dynamic array of random numbers (size: %d)\n", size);
		array = (int*)calloc(size, sizeof(int));
		if (array == NULL) {
			printf("Error in dynamic memory allocation for integer array of size (%d)\n", size);
			exit(-1); 
		}
		genBigRandArray(array, size);
		printArraySample(array, size, LINE_SIZE);
		free(array);
	}
	return 0;
}

void genBigRandArray(int* array, int size) {
	int temp;
	unsigned int u_int32 = 0;
	int index_1, index_2;

	for (int i = 0; i < size; i++) {
		array[i] = i + 0;
	}
	for (int i = 0; i < size; i++) {
		u_int32 = ((long)rand() << 15) | rand();
		index_1 = u_int32 % size;
		u_int32 = ((long)rand() << 15) | rand();
		index_2 = u_int32 % size;

		if (index_1 != index_2) {
			temp = array[index_1];
			array[index_1] = array[index_2];
			array[index_2] = temp;
		}
	}
}

void printArraySample(int* array, int size, int line_size) {
	for (int i = 0; i < 30; i++) {
		printf("%8d ", array[i]);
		if ((i + 1) % line_size == 0) {
			printf("\n");
		}
	}
	printf("\n");
	for (int i = size - 30; i < size; i++) {
		printf("%8d ", array[i]);
		if ((i - (size - 30) + 1) % line_size == 0) {
			printf("\n");
		}
	}
	printf("\n");
}