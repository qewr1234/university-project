#include <iostream>
#include <cstring>

using namespace std;

int main(){

    struct Product0{
        int idType;
        int idInteger;
        char idchars[10];
    };

    union ID{
        int integer;
        char chars[10];
    };
// union�� �޸𸮸� ���� ȿ�������� ����ϱ� ���� ���δ�

    struct Product1{
        int idType;
        ID id;
    };

    Product0 product0 = {0, 12};
    if (product0.idType == 0)
        cout << product0.idInteger << endl;
    else
        cout << product0.idchars << endl;

    Product1 product1 = {1, {.chars = "abc"}};
    if (product1.idType == 0)
        cout << product1.id.integer << endl;
    else
        cout << product1.id.chars << endl;

    cout << "Prodcut0�� ������� = " << sizeof(Product0) << endl;
    cout << "Prodcut1�� ������� = " << sizeof(Product1) << endl;
}