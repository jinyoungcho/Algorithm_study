//
//  main.cpp
//  example_21_2294_dp
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;
int n_coin, k;
int arr[101];
int dp[100001];


int main(int argc, const char * argv[]) {
    
    cin >> n_coin >> k;
    for(int i=0; i<n_coin; i++){
        cin >> arr[i];
    }
    for(int i=0; i<100001; i++){
        dp[i] = 100001;
    }
    dp[0]=0;
    
    for(int i=0; i<n_coin; i++){
        int coin = arr[i];
        
        for(int j=coin; j<=k; j++){
            dp[j] = min(dp[j], dp[j-coin]+1);
        }
    }
    
    if (dp[k] == 100001){
        cout << -1 << endl;
    }else{
        cout << dp[k] << endl;
    }
//
//
//    for(int i =0; i<n_coin; i++){
//        cout << arr[i] << ',';
//    }
//    cout << endl;
//    for(int i =0; i<=k; i++){
//        cout << dp[i] << ',';
//    }
    // insert code here...
    return 0;
}
