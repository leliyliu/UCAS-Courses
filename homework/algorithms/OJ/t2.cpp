#include<iostream>
#include<vector> 
using namespace std;

int minbinsearch(vector<int> &nums, int target, int l, int r){
    bool end = (l>r);
    if(end) 
        return -1;
    int mid;
    while(l<r){
        mid = (l+r)>>1;
        bool less = (nums[mid] < target);
        if(less)
            l = mid+1; 
        else 
            r = mid;
    }
    bool equal = (nums[l] == target);
    if(equal)
        return l;
    else
        return -1;
}

int maxbinsearch(vector<int> &nums, int target, int l, int r){
    bool end = (l>r);
    if(end) 
        return -1;
    int mid; 
    while(l<r){
        mid = (l+r+1)>>1;
        bool more = (nums[mid] > target);
        if(more)
            r = mid-1;
        else
            l = mid;
    }
    bool equal = (nums[r] == target);
    if(equal)
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
        bool equal = (left == -1);
        if(equal)
            right = -1;
        else
            right = maxbinsearch(nums, target, 0, n-1);
        lefts.push_back(left);
        rights.push_back(right);
    } 
    for(int i=0; i<m; i++){
        cout << lefts[i] << ' ' << rights[i] << endl; 
    }
    return 0;
}

