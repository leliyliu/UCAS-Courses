#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector<int> nums;
    int tmp, prev=0; 
    while(cin>>tmp){
        nums.push_back(tmp);
        char ch = getchar();
        if(ch == '\n')
            break; 
    }
    long sum = 0; 
    for(auto num : nums){
        sum += max(0,  num-prev);
        prev = num;
    }
    cout<<sum;
    return 0;
}