#include <iostream>

using namespace std;

int main(){
    cout << "What is your favorite food?" << endl;
    cout << "1) Kimch" << endl;
    cout << "2) Korean BBQ" << endl;
    cout << "3) Chicken" << endl;
    cout << ">";

    int num;
    cin >> num;

    switch (num) {
        case 1:
            cout << "You selection Kimch" << endl;
            break;
        case 2:
            cout << "You selection BBQ" << endl;
            break;
        case 3:
            cout << "You selection chicken" << endl;
            break;
        default:
            cout << "Impossible" << endl;
    }
}