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
// union은 메모리를 좀더 효율적으로 사용하기 위해 쓰인다

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

    cout << "Prodcut0의 사이즈는 = " << sizeof(Product0) << endl;
    cout << "Prodcut1의 사이즈는 = " << sizeof(Product1) << endl;
}