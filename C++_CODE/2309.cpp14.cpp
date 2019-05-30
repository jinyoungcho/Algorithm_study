//
//  main.cpp
//  example11_brute-force-search
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool fun(const int x, const int y){
    if (x>y){
        return true;
    }else{
        return false;
    }
}



int main(int argc, const char * argv[]) {
    
    
    int arr[9];
    
    for(int i =0; i<9; i++){
        scanf("%d",&arr[i]);
    }
    
    int short1=-1;
    int short2=-1;
    sort(arr,arr+9);
    bool done = false;
    int sum = 0;

    for(int i = 0; i<9; i++){
        for(int j = 0; j<9; j++){
            sum = 0;
            if (i==j){
                continue;
            }else{
                
                for(int k = 0; k < 9; k++){
                    if( k!=i and k!=j ){
                        sum+= arr[k];
                    }
                }
                
                if (sum == 100){
                    done = true;
                    short1 = i;
                    short2 = j;
                }
            }
        }
        if(done==true){
            break;
        }
    }
    
    for(int i =0; i<9; i++){
        if (i != short1 and i != short2){
            cout << arr[i]<<endl;
        }
        
    }
    
}


