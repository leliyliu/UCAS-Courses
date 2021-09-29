#include<iostream>
#include<vector>
#include<string>
using namespace std; 

int div2(vector<int>& b){
    int cur, nxt = 0; 
    for(auto iter=b.begin(); iter!=b.end(); iter++){
        cur = *(iter) + 10*nxt;
        *(iter) = cur>>1;
        nxt = (cur&1);
    }
    auto iter = b.begin();
    if(*(iter) == 0)
        b.erase(iter);
    return nxt; 
}

int superPow(int a, vector<int>& b) {
    if(a==1)
        return 1;
    if(a==0)
        return 0;
    int remainder, res;
    if(b.empty())
        return 1;
    else{
        remainder = div2(b);
        res = (superPow(a, b)%1337);
        res = (res*res)%1337;
        if(remainder&1){
            return ((a%1337)*res)%1337;
        }
        else{
            return res;
        }
    }
}

int main(){
    int a, tmp;
    vector<int> b; 
    string str; 
    cin>>a; 
    getchar();
    getline(cin, str);
    for(auto iter=str.begin(); iter!=str.end(); iter++){
        if(isdigit(*(iter))){
            tmp = (int) (*(iter) - '0');
            b.push_back(tmp);
        }
    }
    int res = superPow(a, b);
    cout<<res;
    return 0; 
}