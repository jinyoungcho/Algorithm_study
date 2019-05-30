//
//  main.cpp
//  example_15_2503_bf
//
//  Created by 조진영 on 21/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;


bool arr[1000];
string temp;

int testcase;

int main(int argc, const char * argv[]) {
    for(int i=123; i<=999; i++){
        temp=to_string(i);
        
        if (temp[0] == '0' or temp[1] == '0' or temp[2] == '0'){
            arr[i] = false;
        }else if(temp[0] == temp[1] or temp[1] == temp[2] or temp[2] == temp[0]){
            arr[i] = false;
        }else{
            arr[i] = true;
        }
    }
    
//    string asdf = "012";
//    cout << (asdf[0] == '0') << endl;
//
//    cout << arr[708];

    
    cin >> testcase;
    
    int numbers;
    int strike;
    int ball;
    
    while(testcase--){
        cin >> numbers >> strike >> ball;
        
        string first = to_string(numbers);
        

        
        for(int i=123; i<=999; i++){
            
            int strike_cnt = 0;
            int ball_cnt = 0;
            
            if (arr[i] == true){
                string second = to_string(i);
                
                for(int x=0; x<3; x++){
                    for(int y=0; y<3; y++){
                        //strike check;
                        if(x==y and first[x] == second[y]){
                            strike_cnt++;
                        }
                        
                        //ball check;
                        if(x!=y and first[x] == second[y]){
                            ball_cnt++;
                        }
                    }
                }
                
//                printf("%d, %d\n", strike, strike_cnt);
                
                if (strike == strike_cnt and ball == ball_cnt){
                    arr[i] = true;
                }else{
                    arr[i] = false;
                }
            }
        }
        

        
    }
    int ans=0;
    
    for(int i = 123; i <= 999; i++){
        if (arr[i]){
//            cout << i<< endl;
            ans++;
        }
    }
    
    cout << ans << endl;

}
