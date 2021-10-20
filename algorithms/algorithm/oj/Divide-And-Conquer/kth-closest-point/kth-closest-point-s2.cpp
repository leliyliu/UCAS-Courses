#include<iostream>
#include<algorithm>
using namespace std;

const int N = 5000000;
int n, k;
struct node {
    long long x_label;
    long long y_label;
}nodes[N];

bool cmp(struct node x, struct node y) {
    return (x.x_label * x.x_label + x.y_label * x.y_label) < (y.x_label * y.x_label + y.y_label * y.y_label);
}

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld", &nodes[i].x_label, &nodes[i].y_label);
    sort(nodes, nodes + n, cmp);
    printf("%lld %lld\n", nodes[k-1].x_label, nodes[k-1].y_label);
    return 0;
}