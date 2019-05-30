//
//  main.cpp
//  example05_2675_str_input
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    
    int testcase;
    cin >> testcase;
    
    while(testcase--){
        
        string sample_str;
        int n;
        
        cin >> n >> sample_str;
        
        for(int i=0; i<sample_str.size(); i++){
            for(int j=0; j<n; j++){
                printf("%c", sample_str[i]);
            }
        }
        printf("\n");
        
        
        
    }
    
    return 0;
}
