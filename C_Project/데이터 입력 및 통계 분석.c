#include<stdio.h>
#include<math.h>

void input_data(int arr[], int num);
void print_array(int arr[], int num);
void get_statistics(int arr[], int num, int* min, int* max, double* avg, double* var, double* std);

int main() {
	int arr[100];
	int num, min, max;
	double avg, var, std;

	printf("input number of data to be processed (max 100) = ");
	scanf_s("%d", &num);
	input_data(arr, num);
	printf("input_data = \n");
	print_array(arr, num);
	get_statistics(arr, num, &min, &max, &avg, &var, &std);
	printf("min = %d, max = %d, avg = %lf, var = %lf, std = %lf\n", min, max, avg, var, std);
}

void input_data(int arr[], int num) {
	printf("input %d interger data: ", num);
	for (int i = 0; i < num; i++) {
		scanf_s("%d", &arr[i]);
	}
}

void print_array(int arr[], int num) {
	int count = 0;
	while (count < num) {
		for (int i = 0; i < 10; i++) {
			printf("%5d ", arr[count]);
			count++;
			if (count >= num)
				break;
		}
		printf("\n");
	}
	printf("\n");
}

void get_statistics(int arr[], int num, int* min, int* max, double* avg, double* var, double* std) {
	double sum = 0.0;
	double sum_diff_sq = 0.0, diff, diff_sq;
	*min = *max = arr[0];
	sum = arr[0];

	for (int i = 0; i < num; i++) {
		if (arr[i] < *min)
			*min = arr[i];
		if (arr[i] > *max)
			*max = arr[i];
		sum += arr[i];
	}
	*avg = sum / num;
	
	for (int i = 0; i < num; i++) {
		diff = *avg - arr[i];
		diff_sq = diff * diff;
		sum_diff_sq += diff_sq;
	}

	*var = sum_diff_sq / num;
	*std = sqrt(*var);
}

