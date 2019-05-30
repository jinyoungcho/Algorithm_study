//
//  main.cpp
//  example06_1100_str_Array
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

char Map[8][8];

int main(int argc, const char * argv[]) {
    // insert code here...
    
    for(int i = 0; i < 8; i++){
        scanf("%s", Map[i]);
    }
    
    int cnt = 0;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j<8; j++){
            if( (i+j) % 2 == 0 and Map[i][j] =='F'){
                cnt+=1;
            }
        }
    }
    cout << cnt;
    
    return 0;
}
