#include<iostream>
#include<vector>
#include<string>
using namespace std;

int base = 1337;
int basepow(int a, int k) { // 这里 k < 10 
    a %= base;
    int res = 1;
    for (int i = 0; i < k; i++) {
        res *= a;
        res %= base;
    }
    return res;
}

int superPow(int a, vector<int>& b) {
    if (b.empty()) return 1;
    int last = b.back();
    b.pop_back();
    
    int part1 = basepow(a, last);
    int part2 = basepow(superPow(a, b), 10);
    // 每次乘法都要求模
    return (part1 * part2) % base;
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