#include <iostream>

using namespace std;

const int N = 200200;
char str[N] = "";
char in;
long long ind = -1;

int main()
{
    while (1) {
        in = getchar();
        if (in == '\n')
            break;
        if (ind < 0) {
            ind++;
            str[ind] = in;
        }
        else if (in == 'B')
            ind--;
        else {
            ind++;
            str[ind] = in;
        }
    }
    printf("%lld", ind + 1);
    return 0;
}