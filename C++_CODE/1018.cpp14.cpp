//
//  main.cpp
//  example16_1018_bf
//
//  Created by 조진영 on 21/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
using namespace std;

char arr[50][50];
int n,m;

char black_[8][8] = {
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'}
};
char white_[8][8] ={
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'},
    {'W','B','W','B','W','B','W','B'},
    {'B','W','B','W','B','W','B','W'}
};

int check_black(int i, int j){
    int cnt_b = 0;
    
    for(int x=i; x<i+8; x++){
        for(int y=j; y<j+8; y++){
            if (black_[x-i][y-j] != arr[x][y]) {
                cnt_b++;
            }
        }
    }
    return cnt_b;
}

int check_white(int i, int j){
    
//    for(int x=i; x<i+8; x++){
//        for(int y=j; y<j+8; y++){
//            cout << arr[x][y];
//        }
//        cout << endl;
//    }
//    printf("-----");

    
    int cnt_w = 0;
    for(int x=i; x<i+8; x++){
        for(int y=j; y<j+8; y++){
            if (white_[x-i][y-j] != arr[x][y]) {
                cnt_w++;
            }
        }
    }
    return cnt_w;
}

int mini = 100000;
int main(int argc, const char * argv[]) {
    // insert code here...
    // i = n; j = m;
    cin >> n >> m;
    
    for(int i = 0; i<n; i++){
        cin >> arr[i];
    }
    
    for(int i=0; i<=n-8; i++){
        for(int j=0; j<=m-8; j++){
            
            int b_cnt = check_black(i,j);
            
            int w_cnt = check_white(i,j);
            
            int cnt = min(b_cnt, w_cnt);
            
//            printf("%d, %d\n",b_cnt, w_cnt);
            
            mini = min(mini, cnt);
        }
    }
    cout << mini << endl;
}
