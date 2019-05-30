//
//  main.cpp
//  example_28_9019_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cstring>
#include <utility>
#include <string>
using namespace std;




int T;
int Start;
int End;
bool c[10000];
int main(int argc, const char * argv[]) {

    cin >> T;
    while(T--){
        cin >> Start >> End;
        memset(c,false,sizeof(c));
        queue<pair<int,string>> q;
        q.push(make_pair(Start,""));
        c[Start] = true;
        
        while(!q.empty()){
            int now = q.front().first;
            string change = q.front().second;
            q.pop();
            
            if(now == End){
                cout << change <<endl;
                break;
            }
            
            //D
            int d = now*2;
            if(d>9999){
                d = d%10000;
            }
            
            if(c[d] == false){
                c[d] = true;
                q.push(make_pair(d, change+"D"));
            }
            
            //S
            int s;
            if(now==0){
                s = 9999;
            }else{
                s = now-1;
            }
            if(c[s] == false){
                c[s] = true;
                q.push(make_pair(s, change+"S"));
            }
            
//            string str = to_string(now);
//            int str_len = str.size();
//            for(int i=0; i<(4-str_len);i++){
//                str = "0" + str;
//            }
            
            //L
//            string ll = {str[1],str[2],str[3],str[0]};
//            int l = atoi(ll.c_str());
            int l = (now % 1000) * 10 + now / 1000;
            
            
            
            if(c[l] == false){
                c[l] = true;
                q.push(make_pair(l, change+"L"));
            }
            
            //R
//            string rr = {str[3],str[1],str[2],str[3]};
//            int r = atoi(rr.c_str());


            int r = (now % 10) * 1000 + (now / 10);
//            cout << now << "-" << r << endl;
            if(c[r] == false){
                c[r] = true;
                q.push(make_pair(r, change+"R"));
            }
        }
        
        
    }
    
    return 0;
}
