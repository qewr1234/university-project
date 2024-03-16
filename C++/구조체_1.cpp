#include <iostream>
#include <cstring>

using namespace std;

int main(){
    struct EYESIGHT{
        float left;
        float right;

    };
    struct Person{
        float height;
        float weight;
        char name[10];
        short grade;
        EYESIGHT eyesight;
    };
    Person person0 = {174.3, 73, "LEE", 1, {1.1f, 1.0f}};
    Person person1 = person0;

    cout << person1.height << endl;
    cout << person1.weight << endl;
    cout << person1.grade << endl;
    cout << person1.name << endl;
    cout << person1.eyesight.left << endl;
    cout << person1.eyesight.right << endl;
}