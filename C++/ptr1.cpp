#include <iostream>

using namespace std;

int main(){
    int num = 147;
    int *ptr = &num;

    cout << num << endl;
    cout << ptr << endl;
    cout << &num << endl;
    cout << *ptr << endl;

    *ptr = 100;
    cout << *ptr << endl;
}