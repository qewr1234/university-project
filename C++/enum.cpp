#include <iostream>

using namespace std;

enum Color{
    Red, Green, Blue
};

int main(){
    int Colors[3] = {255, 128, 64};
    int total = 0;

    cout << "Red: " << Colors[Red] << endl;
    cout << "Green: " << Colors[Green] << endl;
    cout << "Blue: " << Colors[Blue] << endl;

    for(int i = 0; i < 3; i++){
        total += Colors[i];
    }

    int avg0 = total / 3;

    cout << avg0 << endl;


}