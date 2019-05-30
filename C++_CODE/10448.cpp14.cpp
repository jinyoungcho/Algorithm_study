//
//  main.cpp
//  example14_10448_bf
//
//  Created by 조진영 on 21/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
using namespace std;
int Testcase;
int tri[45];

int fuc(int asdf){
    for(int i = 0; i<45; i++){
        for(int j = 0; j<45; j++){
            for(int k = 0; k<45; k++){
                if (tri[i]+tri[j]+tri[k] == asdf){
//                    cout<<tri[i] << tri[j] << tri[k] <<endl;
                    return 1;
                }
            }
        }
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    
    for(int i=1; i<46; i++){
        tri[i-1] = i*(i+1)/2;
    }

    
    
//    for(int i=0; i<45; i++){
//        cout<< tri[i] <<endl;
//    }
    
    cin >> Testcase;
    int n;
    while(Testcase--){
        cin >> n;
        cout << fuc(n) <<endl;
    }
    
    return 0;
}
