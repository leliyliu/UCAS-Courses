#include<iostream>
#include<string>
#include<unordered_map>
#include<vector>
using namespace std; 

vector<int> partition(string s) {
    unordered_map<char, int> last;
    vector<int> res; 
    int n=s.length();
    for(int i=0;i<n;i++){
        last[s[i]] = i;
    }
    int begin=0, end;
    while(begin<n){
        end = last[s[begin]];
        for(int i=begin+1;i<end;i++){
            if(last[s[i]] > end)
                end = last[s[i]];
        }
        res.push_back(end-begin+1);
        begin=end+1;
    }
    return res;
}

int main(){
    string str; 
    cin>>str;
    auto result = partition(str);
    for(auto iter=result.begin(); iter!=result.end(); iter++){
        cout<<*iter<<" ";
    }
}