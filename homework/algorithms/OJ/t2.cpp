#include<iostream>
#include<vector> 
using namespace std;

int minbinsearch(vector<int> &nums, int target, int l, int r){
    if(l>r) 
            return -1;
    int mid;
    while(l<r){
        mid = (l+r)>>1;
        if(nums[mid] < target)
            l = mid+1; 
        else 
            r = mid;
    }
    if(nums[l] == target)
        return l;
    else
        return -1;
}

int maxbinsearch(vector<int> &nums, int target, int l, int r){
    if(l>r) 
            return -1;
    int mid; 
    while(l<r){
        mid = (l+r+1)>>1;
        if(nums[mid] > target)
            r = mid-1;
        else
            l = mid;
    }
    if(nums[r] == target)
        return r;
    else
        return -1;
}

int main(){
    int n, m, target, tmp, left, right;
    vector<int> nums, lefts, rights;
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>tmp; 
        nums.push_back(tmp);
    }
    for(int i=0; i<m; i++){
        cin>>target;
        left = minbinsearch(nums, target, 0, n-1);
        if(left == -1)
            right = -1;
        else
            right = maxbinsearch(nums, target, 0, n-1);
        lefts.push_back(left);
        rights.push_back(right);
    } 
    for(int i=0; i<m; i++){
        if(i!=m-1)
            cout << lefts[i] << ' ' << rights[i] << endl; 
        else
            cout << lefts[i] << ' ' << rights[i];
    }
    return 0;
}

