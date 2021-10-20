#include<iostream>

using namespace std;

int result;
int m;
int n;

int calculate(int n) {
    if (n == 1)
        return m;
    int res1 = calculate(n / 2);
    if (n % 2 == 1)
        return abs(res1 * res1 * m % 1000);
    else
        return abs(res1 * res1 % 1000);
}

int main() {
    scanf("%d %d", &m, &n);
    if (m == 0) {
        printf("0\n");
        return 0;
    }
    if (n == 0) {
        printf("1\n");
        return 0;
    }
    m = abs(m);
    m = m % 1000;
    result = calculate(n);
    printf("%d\n", result);
    return 0;
}