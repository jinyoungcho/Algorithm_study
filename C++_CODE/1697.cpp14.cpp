//
//  main.cpp
//  example_30_1697_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

int g[100001];
int N;
int M;

int main(int argc, const char * argv[]) {
    
    memset(g, -1, sizeof(g));
    
    cin >> N >> M;
    
    queue<int> q;
    q.push(N);
    g[N] = 0;
    
    while(!q.empty()){
        int n = q.front(); q.pop();
        
        int n1 = n-1;
        int n2 = n+1;
        int n3 = n*2;
        if(0<= n1 and n1 <=100000){
            if(g[n1] == -1){
                g[n1] = g[n]+1;
                q.push(n1);
            }
        }
        if(0<= n2 and n2 <=100000){
            if(g[n2] == -1){
                g[n2] = g[n]+1;
                q.push(n2);
            }
        }
        if(0<= n3 and n3 <=100000){
            if(g[n3] == -1){
                g[n3] = g[n]+1;
                q.push(n3);
            }
        }
    }
    
    if(N == M){
        cout << 0 << endl;
    }else if(g[M] != -1){
        cout << g[M]<<endl;
    }
    
//    for(int i =0; i<=M ;i++){
//        cout << g[i] <<' ';
//    }
    
    return 0;
}
