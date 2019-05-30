//
//  main.cpp
//  example_29_7576_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cstring>
#include <utility>

using namespace std;

int N;
int M;

int g[1002][1002];
int di[] = {0,0,1,-1};
int dj[] = {1,-1,0,0};

int main(int argc, const char * argv[]) {
    cin >> M >> N;
    
    queue<pair<int,int>> q;
    
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> g[i][j];
            if(g[i][j] == 1){
                q.push(make_pair(i,j));
            }
        }
    }
    
//    for(int i=0; i<N; i++){
//        for(int j=0; j<M; j++){
//            cout <<g[i][j]<<' ';
//        }
//        cout << endl;
//    }
    
    while(!q.empty()){
        int i = q.front().first;
        int j = q.front().second;
        q.pop();
        
        for(int k=0; k<4; k++){
            int ni = i+di[k];
            int nj = j+dj[k];
            
            if(0<= ni and ni<N and 0<= nj and nj<M){
                if(g[ni][nj] == 0){
                    g[ni][nj] = g[i][j]+1;
                    q.push(make_pair(ni, nj));
                }
            }
        }
    }
    
//    cout << endl;
//    cout << N << M << endl;
    int maxi=-10000000;
    bool all=true;
    
    for(int i=0; i<N;i++){
        for(int j=0; j<M; j++){
//            cout << g[i][j] <<' ';
            if(g[i][j] == 0){
                all = false;
            }else{
                maxi = max(maxi, g[i][j]);
            }
        }
//        cout << endl;
    }
    
    if(all == true){
        cout << maxi-1 << endl;
    }else{
        cout << -1 << endl;
    }
    return 0;
}
