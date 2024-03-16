#include <iostream>

using namespace std;

int main(){
    int nums[4]{10, 11, 12};
    int size = sizeof(nums) / sizeof(int);

    for(int i = 0; i < size; i++) {
        cout << nums[i] << endl;
    }
    cout << size << endl;
}