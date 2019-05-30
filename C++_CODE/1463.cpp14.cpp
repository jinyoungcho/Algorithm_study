//
//  main.cpp
//  example_19_1463_dp
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int N;
vector<int> dp;

int fuc(int n){
    if(n == 1){return dp[1];}
    if(dp[n]){
        return dp[n];
    }
    
    dp[n] = fuc(n-1) + 1;
    
    if(n%2 == 0){
        dp[n] = min(fuc(n/2) + 1, dp[n]);
    }
    if(n%3 == 0){
        dp[n] = min(fuc(n/3) + 1, dp[n]);
    }
    
    
    
    return dp[n];
}

int main(int argc, const char * argv[]) {
    cin >> N;
    dp.resize(N+1);
    dp[0] = 0;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    
    int ans = fuc(N);
    
//    for(int i=0; i<N+1; i++){
//        cout << dp[i] << ',';
//    }
//    cout << endl;
    cout << ans << endl;
    
    
    return 0;
}
