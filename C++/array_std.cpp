#include <iostream>
#include <array>

using namespace std;

int main(){
    /*array <int, 5> arr{1, 2, 3};
    cout << arr[-1] << endl;
    cout << arr[10] << endl;
    cout << arr.at(1) << endl;
    cout << arr.size() << endl;
    */
    array <int, 5> arr0{1, 2, 3, 4, 5};
    array <int, 5> arr1{5, 4, 3, 2, 1};
    array <char, 6> arr2{"abcde"}; /* 뒤에 NULL문자가 있어야해서 배열의 크기가 1 더 크다

    arr0.swap(arr1); /* arr0과 arr1위치 변경 */

    for (int i = 0; i < arr0.size(); i++)
        cout << arr0[i];
    cout << endl;

    for (int i = 0; i < arr1.size(); i++)
        cout << arr1[i];
    cout << endl;

    cout << arr0.data()[0] << endl;

    for (int i = 0; i < arr2.size(); i++)
        cout << arr2[i];
}