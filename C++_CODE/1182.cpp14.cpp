//
//  main.cpp
//  example_17_1182_bf
//
//  Created by 조진영 on 21/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;


int n, s;
int arr[21];

int cnt=0;

void rec(int index, int ss){
//    cout << index <<endl;
    if(index == n){
        if(ss == s){
            cnt++;
        }
        return;
    }
    //선택 한다;
    rec(index+1, ss+arr[index]);
    //선택 안한다;
    rec(index+1, ss);
}

int main(int argc, const char * argv[]) {
    // insert code here...

    cin >> n >> s;
    for(int i = 0; i<n; i++){
        cin >> arr[i];
    }
    rec(0, 0);
    
    if (s == 0){
        cout << cnt-1 << endl;
    }else{
        cout << cnt << endl;
    }
}
