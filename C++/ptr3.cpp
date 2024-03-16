#include <iostream>

using namespace std;

int main(){
    int nums[] = {5, 45, 1};
    int *pNums = nums;

    cout << nums << endl;
    cout << &nums << endl;
    cout << &nums[0] << endl;
    cout << " " << endl;

    cout << *pNums << endl;
    cout << *(pNums + 1) << endl;
    cout << *(pNums + 2) << endl;
    cout << " " << endl;

    cout << *pNums << endl;
    pNums++;
    cout << *pNums << endl;
    cout << " " << endl;

    cout << typeid(&nums).name() << endl;
}