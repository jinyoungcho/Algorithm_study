//
//  main.cpp
//  example04_10953
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int testcase;
    cin >> testcase;
    
    while(testcase--){
        int a,b;
        scanf("%d,%d",&a,&b);
        printf("%d\n",a+b);
    }
    
    return 0;
}
