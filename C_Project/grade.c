#include <stdio.h>

int main(void) {
	int score = 0;
	char grade = 0;

	while(1){
		printf("������ �Է��Ͻÿ�.: ");
		scanf_s("%d", &score);

		if (score > 100) {
			printf("�����Դϴ�");
			break;
		}
		else if (score >= 90)
			grade = 'A';
		else if (score >= 80)
			grade = 'B';
		else if (score >= 70)
			grade = 'C';
		else if (score >= 60)
			grade = 'D';
		else
			grade = 'F';

		printf("���: %c\n", grade);
	}


	return 0;
}