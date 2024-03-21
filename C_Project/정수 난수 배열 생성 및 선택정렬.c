#include <stdio.h>
#include <random>
#define NUM 100

void random_arr(int arr[]);
void print_arr(int arr[]);
void selection_sort(int arr[], int size);

int main() {
	int arr[NUM];

	srand((unsigned)time(NULL));

	printf("Random array(size = 100) before sorting: \n");
	random_arr(arr);
	print_arr(arr);

	printf("Random array(size = 100) after sorting: \n");
	selection_sort(arr, NUM);
	print_arr(arr);
}

void random_arr(int arr[]) {
	for(int i = 0; i < NUM; i++){
		arr[i] = rand() % 1000;
	}
}

void print_arr(int arr[]) {
	int count = 0;
	while (count < NUM) {
		for (int i = 0; i < 20; i++) {
			printf("%5d ", arr[count]);
			count++;
			if (count >= NUM)
				break;
		}
		printf("\n");
	}
	printf("\n");
}

void selection_sort(int arr[], int size) {
	int index_min;
	int min_value;

	for (int round = 0; round < size - 1; round++) {
		index_min = round;
		min_value = arr[index_min];
		for (int j = round + 1; j < size; j++) {
			if (arr[j] < min_value) {
				index_min = j;
				min_value = arr[j];
			}
		}
		if (index_min != round) {
			arr[index_min] = arr[round];
			arr[round] = min_value;
		}
	}
}