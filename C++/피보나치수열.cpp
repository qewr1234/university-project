#include <iostream>

using namespace std;

int main(){
    int num;
    int PreValue = 0;
    int CurrValue = 1;

    cin >> num;

    if (num == 0){
        cout << 0 << endl;
    }
    else if (num == 1){
        cout << 1 << endl;
    }
    else{

        for (int i = 0; i < num - 1; ++i){
            int NextValue = PreValue + CurrValue;
            PreValue = CurrValue;
            CurrValue = NextValue;
        }
        cout << CurrValue << endl;
    }
}