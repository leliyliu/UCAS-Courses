#include <iostream>

using namespace std;

const int N = 1000;
int status[N][N];
int unbrokenSteps[N];
int n;


int whetherCanClimbing() {
    int canClimbing = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            int k = unbrokenSteps[i] - unbrokenSteps[j];
            if (k <= j + 1) {
                status[i][k] = (status[j][k - 1] || status[j][k] || status[j][k + 1]);
            }
            if (i == n - 1 && status[i][k] == 1)  canClimbing = 1;
        }
    }
    return canClimbing;
}

int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &unbrokenSteps[i]);
    }
    // initialization
    if (n == 1) {
        printf("true");
        return 0;
    }
    if (unbrokenSteps[1] != 1) {
        printf("false");
        return 0;
    }
    memset(status, 0, sizeof(status));
    status[0][0] = 1;
    int result = whetherCanClimbing();
    if (result) 
        printf("true");
    else 
        printf("false");
    return 0;
}