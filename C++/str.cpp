#include <iostream>
#include <cstring>

using namespace std;

int main(){
    string str0("abc");
    string str1("abc");

    str0 += str1;

    cout << str0 << endl;
}