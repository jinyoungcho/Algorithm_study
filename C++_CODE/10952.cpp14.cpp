//
//  main.cpp
//  example03_10952
//
//  Created by 조진영 on 20/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
using namespace std;
int main(){
    int a, b;
    while(scanf("%d%d", &a, &b)!=EOF)
        
        if(a == 0 and b == 0){
            break;
        }else{
            printf("%d\n", a+b);
        }
        
    
    return 0;
}
