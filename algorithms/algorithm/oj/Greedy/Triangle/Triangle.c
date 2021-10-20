#include <iostream>
#include <algorithm>

using namespace std;

const int N = 100200;
long long seg[N];
long long length;
int flag = 0;

int main()
{
    scanf("%lld", &length);
    for (int i = 0; i < length;i++) {
        scanf("%lld", &seg[i]);
    }
    sort(seg, seg + length);

    for (int i = 1; i < length - 1; i++) {
        if (seg[i - 1] + seg[i] < 0)
            continue;
        if (seg[i - 1] + seg[i] > seg[i + 1]) {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
        printf("YES\n");
    else
        printf("NO\n");

    return 0;
}