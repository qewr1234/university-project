# include <stdio.h>

int main(void) {
	int prices, shipping_fee;
	char loc;

	printf("제품의 가격을 입력하세요.: ");
	scanf_s("%d", &prices);

	getchar(); // 앞쪽 버퍼가 남아있기 때문에 getchar또는 scanf_s(" %c", &loc, 1)형태로 써야함

	printf("배송 위치를 입력하세요.: ");
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
		printf("유효하지 않은 위치입니다.");
		return 1;
	}
	
	printf("배송비는 %d원 입니다", shipping_fee);

	return 0;
}
