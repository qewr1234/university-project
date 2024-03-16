#include <iostream>

using namespace std;

int main(){
    int nums[] = {5, 4, 3, 1, 7, 5, 3, 9, 6, 1, 2};

    for(int i = 0; i < size(nums); i++){
        for (int j = 0; j < size(nums) - 1 - i; j++){
            if(nums[j] > nums[j + 1]){
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < size(nums); i++){
        cout << nums[i] << endl;
    }
}