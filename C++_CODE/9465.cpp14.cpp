//
//  main.cpp
//  example_20_9465_dp
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
int testcase;
int num_stickers;

int arr[2][100001];
int dp[2][100001];



int main(int argc, const char * argv[]) {
    
    cin >> testcase;
    while(testcase--){
        cin >> num_stickers;
        
        //입력
        for(int i=0; i<2; i++){
            for(int j=0; j<num_stickers; j++){
                cin >> arr[i][j];
            }
        }
        dp[0][0] = arr[0][0];
        dp[1][0] = arr[1][0];
        
        
        for(int i=1; i<num_stickers; i++){
            dp[0][i] = max( dp[1][i-1], dp[1][i-2] ) + arr[0][i];
            dp[1][i] = max( dp[0][i-1], dp[0][i-2] ) + arr[1][i];
        }

        cout << max(dp[0][num_stickers-1], dp[1][num_stickers-1]) << endl;;
        
    }
    

    
    return 0;
}



//for(int i=0; i<2;i++){
//    for(int j=0; j<num_stickers;j++){
//        cout << arr[i][j] <<',';
//        }
//        cout << endl;
//        }
//        cout << endl;
