//
//  main.cpp
//  example_32_1525_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <map>
using namespace std;

int di[] = {0,0,1,-1};
int dj[] = {1,-1,0,0};

int main(int argc, const char * argv[]) {
    
    string start = "";
    
    string goal = "123456789";
    int k;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            cin >> k;
            if (k == 0){
                k=9;
            }
            start += to_string(k);
        }
    }
    
    map<string,int> visited;
    visited[start] = 0;
    
    queue<string> q;
    q.push(start);
    
    
    while(!q.empty()){
        string cur = q.front(); q.pop();
        string s = cur;
        
        if(s == goal){
            break;
        }
        
        int loc = s.find("9");
        
        int i = loc/3;
        int j = loc%3;
        
        for(int k = 0; k<4 ;k++){
            int ni= i+di[k];
            int nj= j+dj[k];
        
            if(0<= ni and ni<3 and 0<= nj and nj< 3){
                string temp = s;
                swap(temp[3*i+j], temp[3*ni+nj]);
                if(visited.count(temp) != 1){
                    q.push(temp);
                    visited[temp]= visited[cur] +1;
                }
            }
        }
    }
    
    if(visited.count(goal) == 1){
        cout << visited[goal] << endl;
    }else{
        cout << -1 << endl;
    }
    
    return 0;
}
