#include<iostream>
#include<vector>
// #include<math>
using namespace std;


int minimum(vector<vector<int>>& triangle, int n) {
    for(int i=1;i<n;i++){
        triangle[i][0] += triangle[i-1][0];
        for(int j=1;j<i;j++){
            triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j]);
        }
        triangle[i][i] += triangle[i-1][i-1];
    }
    int res = triangle[n-1][0];
    for(int i=1;i<n;i++){
        if(triangle[n-1][i] < res)
            res = triangle[n-1][i];
    }
    return res; 
}

int main(){
    int n, tmp; 
    cin>>n; 
    vector<vector<int>> nums;
    vector<int> tmpvector;
    int i=0,j=0;
    while (cin>>tmp){
        tmpvector.push_back(tmp);
        char ch = getchar();
        if(j==i){
            nums.push_back(tmpvector);
            i++;
            j=0;
            tmpvector.clear();
        }
        else
            j++;
        if(ch == '\n')
            break; 
    }
    cout<<minimum(nums, n);

    return 0;
}