//
//  main.cpp
//  example_27_3055_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <utility>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

char g[52][52];
int r;
int c;
int di[]={0,0,1,-1};
int dj[]={1,-1,0,0};

int main(int argc, const char * argv[]) {
    cin >> r >> c;
    for(int i=0; i<r; i++){
        cin >> g[i];
    }
    
    pair<int, int> S;
    pair<int, int> D;
    vector<pair<int,int>> water;
    
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            if(g[i][j] == 'D'){
                D = make_pair(i,j);
            }else if(g[i][j] == 'S'){
                S = make_pair(i,j);
            }else if(g[i][j] == '*'){
                water.push_back(make_pair(i,j));
            }
        }
    }
    
    
    
    queue<pair<int, int>> water_q;
    int water_g[52][52];
    bool water_c[52][52];
    memset(water_g, -1, sizeof(water_g));
    memset(water_c, false, sizeof(water_c));
    
    for(int i=0; i<water.size();i++){
        water_q.push(water[i]);
        water_g[water[i].first][water[i].second] = 0;
        water_c[water[i].first][water[i].second] = true;
    }
    
    while(!water_q.empty()){
        int i = water_q.front().first;
        int j = water_q.front().second;
        water_q.pop();
        
        for(int k =0; k<4; k++){
            int ni = i+di[k];
            int nj = j+dj[k];
            
            if(0<=ni and ni<r and 0<=nj and nj<c){
                if(water_c[ni][nj]==false and g[ni][nj]=='.'){
                    water_c[ni][nj]=true;
                    water_g[ni][nj] = water_g[i][j]+1;
                    water_q.push(make_pair(ni,nj));
                }
            }
        }
    }
    
//    for(int i=0; i<r; i++){
//        for(int j=0; j<c; j++){
//            if (water_g[i][j]==-1){
//                cout << '-';
//            }else{
//                cout << water_g[i][j];
//            }
//        }
//        cout << endl;
//    }
    
    
    
    
    
    
    
    queue<pair<int, int>> kak_q;
    int kak_g[52][52];
    bool kak_c[52][52];
    memset(kak_g, -1, sizeof(kak_g));
    memset(kak_c, false, sizeof(kak_c));
    
    kak_q.push(S);
    kak_g[S.first][S.second]=0;
    kak_c[S.first][S.second]=true;
    
    while(!kak_q.empty()){
        int i =kak_q.front().first;
        int j =kak_q.front().second;
        kak_q.pop();
        
        for(int k=0; k<4; k++){
            int ni = i+di[k];
            int nj = j+dj[k];
            
            if(0<= ni and ni<r and 0<= nj and nj<c){
                if(kak_c[ni][nj]==false
                   and (g[ni][nj]=='.'
                        or g[ni][nj] =='D')
                   and (water_g[ni][nj] == -1
                        or kak_g[i][j]+1 < water_g[ni][nj])){
                       kak_c[ni][nj] = true;
                       kak_g[ni][nj] = kak_g[i][j]+1;
                       kak_q.push(make_pair(ni,nj));
                }
            }
        }
    }
    
    if(kak_g[D.first][D.second] == -1){
        cout << "KAKTUS" <<endl;
    }else{
        cout << kak_g[D.first][D.second] << endl;
    }
}
