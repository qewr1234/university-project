# include <stdio.h>

int main(void) {
	int prices, shipping_fee;
	char loc;

	printf("��ǰ�� ������ �Է��ϼ���.: ");
	scanf_s("%d", &prices);

	getchar();

	printf("��� ��ġ�� �Է��ϼ���.: ");
	scanf_s("%c", &loc, 1);

	if (loc == 'A') {
		if (prices < 50000)
			shipping_fee = 5000;
		else
			shipping_fee = 0;
	}

	else if (loc = 'B') {
		if (prices < 30000)
			shipping_fee = 3000;
		else
			shipping_fee = 0;
	}

	else {
		printf("��ȿ���� ���� ��ġ�Դϴ�.");
		return 1;
	}
	
	printf("��ۺ�� %d�� �Դϴ�", shipping_fee);

	return 0;
}