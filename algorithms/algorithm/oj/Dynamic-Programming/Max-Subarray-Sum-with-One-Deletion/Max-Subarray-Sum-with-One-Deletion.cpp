#include <iostream>
#include <algorithm>

using namespace std;

int n = 0;
long long arr_i;
long long maxSumNoDel;
long long maxSumDel;
long long maxSum;

void addItem() {
    long long tmp1 = maxSumNoDel;
    long long tmp2 = maxSumDel;
    if (tmp1 <= 0 && arr_i <= 0 && tmp1 + arr_i >= 0)
        maxSumNoDel = arr_i;
    else
        maxSumNoDel = max(tmp1 + arr_i, arr_i); 
    maxSum = max(maxSumNoDel, maxSum);
    if (tmp2 <= 0 && arr_i <= 0 && tmp2 + arr_i >= 0)
        maxSumDel = tmp1;
    else
        maxSumDel = max(tmp1, tmp2 + arr_i);
    maxSum = max(maxSumDel, maxSum);
}

int main()
{
    while (scanf("%lld", &arr_i))
    {
        if (n == 0) {
            maxSumNoDel = arr_i;
            maxSumDel = 0;
            maxSum = arr_i;
            n++;
            if ('\n' == getchar())
                break;
            continue;
        }
        addItem();
        if ('\n' == getchar())
            break;
        n++;
    }
    printf("%lld", maxSum);
    return 0;
}