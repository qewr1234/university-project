#include<iostream>

using namespace std;

int main(){
    int num;
    cin >> num;

    int total = 1;
    for(; num; num--){
        total *= num;
    }
    cout << total << endl;
}
