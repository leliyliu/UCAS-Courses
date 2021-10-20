#include<iostream>

using namespace std;

const int N = 5000100;
int A[N];
int n, k;

void quickfind(int Q[], int start, int end){
    if(start >= end)
        return;
    int i = start - 1,j = end + 1;
    int axle = Q[(start + end) >> 1];
    while(i < j){
        do i++;while(Q[i] > axle);
        do j--;while(Q[i] < axle);
        if(i < j) swap(Q[i], Q[j]);
    }
    if(j >= k - 1) quickfind(Q, start, j);
    else quickfind(Q, j + 1, end);
}

int main(){
    scanf("%d %d", &n, &k);
    for(int i = 0;i < n;i++)scanf("%d", &A[i]);
    quickfind(A, 0, n-1);
    printf("%d", A[k - 1]);
    return 0;
}