//
//  main.cpp
//  example12_2231_bf
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
//     insert code here...
    int n;
    cin >> n;
    bool done = false;
    int s = 1;
    int k = 0;
    
    while(true){
//        cout << s << endl;
        k = 0;
        k+=s;
        int kk = 0;
        while(k != 0){
            kk += k%10;
            k /= 10;
        }
        
        if ( (s+kk) == n){
            done = true;
            break;
        }
        
        if (s==n){
            break;
        }
        s++;
    }
    
    if (done == true){
        cout <<s;
    }else{
        cout <<0;
    }
    
    return 0;
}
