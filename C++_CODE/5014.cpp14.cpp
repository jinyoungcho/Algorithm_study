//
//  main.cpp
//  example_25_5014_bfs
//
//  Created by 조진영 on 23/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
using namespace std;


int F; // 총 건물 크기
int S; // 현재 지점
int G; // 목표 지점
int U; // up
int D; // down

bool c[1000001];
int g[1000001];

int main(int argc, const char * argv[]) {
    cin >> F >> S >> G >> U >> D;
    //10 1 10 2 1
    
    fill_n(g,F,-1);
    fill_n(c,F,false);
    
    queue<int> q;
    q.push(S);
    g[S] = 0;
    c[S] = true;
    while(!q.empty()){
        int s = q.front(); q.pop();
        
        int ns_up = s + U;
        int ns_down = s - D;
        
        if(1<= ns_up and ns_up <=F){
            if(c[ns_up] == false){
                c[ns_up] = true;
                g[ns_up] = g[s]+1;
                q.push(ns_up);
            }
        }
        
        if(1<= ns_down and ns_down <=F){
            if(c[ns_down] == false){
                c[ns_down] = true;
                g[ns_down] = g[s]+1;
                q.push(ns_down);
            }
        }
    }
    
    if (c[G] == false){
        cout << "use the stairs" << endl;
    }else{
        cout << g[G]<<endl;
    }
    
}
