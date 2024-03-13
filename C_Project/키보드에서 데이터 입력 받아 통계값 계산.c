#include <stdio.h>
#include <math.h>
#define MAX_NUM_DATA 100
#define PER_LINE 10

void input_data(int data_array[], int num_data);
void print_array(int data_array[], int num_data, int per_line);
void get_statistics(int data_array[], int num_data, double* avg, double* var, double* std, int* min, int* max); // 프로토타입 수정

int main() {
	int data_array[MAX_NUM_DATA];
	int num_data, min, max;
	double avg, var, std;

	printf("input number of data to be processed (max 100) = ");
	scanf_s("%d", &num_data);
	input_data(data_array, num_data);
	printf("input data = \n");
	print_array(data_array, num_data, PER_LINE);
	get_statistics(data_array, num_data, &avg, &var, &std, &min, &max);
	printf("min = %d, max = %d, avg = %lf, var = %lf, std = %lf", min, max, avg, var, std);

	return 0;
}

void input_data(int data_array[], int num_data) {
	printf("input %d integer data: ", num_data);
	for (int i = 0; i < num_data; i++) {
		scanf_s("%d", &data_array[i]);
	}
}

void print_array(int data_array[], int num_data, int per_line) {
	int cnt = 0;
	while (cnt < num_data) {
		for (int i = 0; i < per_line; i++) {
			printf("%5d ", data_array[cnt]);
			cnt++;
			if (cnt >= num_data)
				break;
		}
		printf("\n");
	}
	printf("\n");
}

void get_statistics(int data_array[], int num_data, double* avg, double* var, double* std, int* min, int* max) {
	double sum = 0.0;
	double sum_diff_sq = 0.0, diff, diff_sq;
	*min = *max = data_array[0];
	for (int i = 1; i < num_data; i++) {
		if (data_array[i] < *min)
			*min = data_array[i];
		if (data_array[i] > *max)
			*max = data_array[i];
		sum += data_array[i];
	}
	*avg = sum / num_data;

	for (int i = 0; i < num_data; i++) {
		diff = *avg - data_array[i];
		diff_sq = diff * diff;
		sum_diff_sq += diff_sq;
	}

	*var = sum_diff_sq / num_data;
	*std = sqrt(*var);
}