#include<iostream>
#include<string>
using namespace std;

bool check(string s) {
    int minnum=0, maxnum=0; 
    for(auto it=s.begin(); it!=s.end(); it++){
        if(*it == '('){
            minnum++;
            maxnum++; 
        }
        else if(*it == ')'){
            minnum=max(0, minnum-1);
            maxnum--;
        }
        else{
            minnum=max(0, minnum-1);
            maxnum++;
        }
        if(maxnum < 0)
            return false;
    }
    return minnum==0;
}

int main(){
    string str; 
    cin>>str; 
    if(check(str)){
        cout<<"True";
    }
    else{
        cout<<"NO";
    }
    return 0; 
}