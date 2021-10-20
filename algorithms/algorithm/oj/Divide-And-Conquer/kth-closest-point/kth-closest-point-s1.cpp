#include<iostream>
using namespace std;

const int N = 5000000;
int n, k;
struct node {
    long long x_label;
    long long y_label;
}nodes[N];

long long dist(struct node samp) {
    return samp.x_label * samp.x_label + samp.y_label * samp.y_label;
}

void quickfind(struct node Q[], int start, int end) {
    if (start >= end)
        return;
    int i = start - 1, j = end + 1;
    long long axle = dist(Q[(start + end) >> 1]);
    while (i < j) {
        do i++; while (dist(Q[i]) < axle);
        do j--; while (dist(Q[j]) > axle);
        if (i < j) {
            swap(Q[i], Q[j]);
        }
    }
    if (j >= k - 1) quickfind(Q, start, j);
    else quickfind(Q, j + 1, end);
}

int main() {
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%lld %lld", &nodes[i].x_label, &nodes[i].y_label);
    quickfind(nodes, 0, n - 1);
    printf("%lld %lld\n", nodes[k-1].x_label, nodes[k-1].y_label);
    return 0;
}