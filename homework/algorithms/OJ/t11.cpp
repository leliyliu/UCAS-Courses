#include<iostream>
#include<vector>
#include<string>
using namespace std;

int base = 1337;
// 计算 a 的 k 次方然后与 base 求模的结果
int mypow(int a, int k) {
    // 对因子求模
    a %= base;
    int res = 1;
    for (int _ = 0; _ < k; _++) {
        // 这里有乘法，是潜在的溢出点
        res *= a;
        // 对乘法结果求模
        res %= base;
    }
    return res;
}

int superPow(int a, vector<int>& b) {
    if (b.empty()) return 1;
    int last = b.back();
    b.pop_back();
    
    int part1 = mypow(a, last);
    int part2 = mypow(superPow(a, b), 10);
    // 每次乘法都要求模
    return (part1 * part2) % base;
}

int main(){
    int a, tmp;
    vector<int> b; 
    string str; 
    cin>>a; 
    getline(cin, str);
    cout<<str; 
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