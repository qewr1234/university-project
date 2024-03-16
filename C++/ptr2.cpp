#include <iostream>

using namespace std;
/*union Union{
    int i;
    float f;
    double d;
};*/

int main() {
    int num = 10;
    int const *pNum = &num;

    int num0 = 20;
    pNum = &num0;

    cout << *pNum << endl;

    /* Union u;

    int *ip = (int*)&u;
    float *fp = (float*)&u;
    double *dp = (double*)&u;

    u.f = 3.14;
    u.d = 1;

    cout << *ip << endl;
    cout << *fp << endl;
    cout << *dp << endl; */
}