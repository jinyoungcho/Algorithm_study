//
//  main.cpp
//  example_26_1260_dfs_bfs
//
//  Created by 조진영 on 23/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cmath>
#include <utility>
#include <memory.h>
#include <string.h>
using namespace std;


int T;
char g[1002][1002];
int dx[] = {0,0,1,-1}; // 동 서 남 북;
int dy[] = {1,-1,0,0};

int main(int argc, const char * argv[]) {
    
    cin >> T;
    
    while(T--){
        int c; //j
        int r; //i
        int person_i=0;
        int person_j=0;

        vector<pair<int,int>> fire_pair_vector;
        cin >> c >> r;
        
        
        for(int i=0; i<r; i++){
            cin >> g[i];
        }
        
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if (g[i][j]=='@'){
                    person_i=i;
                    person_j=j;
                }else if(g[i][j]=='*'){
                    fire_pair_vector.push_back(make_pair(i,j));
                }
            }
        }
//        cout << r << c << endl;
//        cout <<"fire!!"<<endl;
//        for(int i =0; i<fire_pair_vector.size(); i++){
//            cout << fire_pair_vector[i].first << fire_pair_vector[i].second << endl;
//        }
//
//        cout << endl;
//        for(int i=0; i<r; i++){
//            for(int j=0; j<c; j++){
//                cout << g[i][j];
//            }
//            cout << endl;
//        }
        

        int fire_g[r][c];
        memset(fire_g,-1,sizeof(fire_g));
    
        bool fire_c[r][c];
        memset(fire_c,false,sizeof(fire_c));
        
        queue<pair<int,int>> fire_q;
        
        for(int i =0; i<fire_pair_vector.size(); i++){
            fire_q.push(fire_pair_vector[i]);
            fire_c[fire_pair_vector[i].first][fire_pair_vector[i].second] = true;
            fire_g[fire_pair_vector[i].first][fire_pair_vector[i].second] = 0;
        }
        
        while(!fire_q.empty()){
            int i= fire_q.front().first;
            int j= fire_q.front().second;
            fire_q.pop();
            
//            cout << i << ',' << j << " now!"<<endl;
            
            for(int k=0; k<4; k++){
                int ni = i+dx[k];
                int nj = j+dy[k];
                
//                cout << ni << ',' << ni <<endl;
                if(0<=ni and ni<r and 0<=nj and nj<c){
                    
                    if(fire_c[ni][nj] == false and g[ni][nj] != '#'){
                        fire_c[ni][nj] = true;
                        fire_g[ni][nj] = fire_g[i][j] +1;
                        fire_q.push(make_pair(ni, nj));
                    }
                }
            }
//            cout << "---" <<endl;
        }
        
        
        
//        cout << endl;
//        for(int i=0; i<r; i++){
//            for(int j=0; j<c; j++){
//                cout << fire_g[i][j] << ' ';
//            }
//            cout << endl;
//        }
//        cout << endl;
        
        
        //사람
        
        int person_g[r][c]; memset(person_g,-1,sizeof(person_g));
        int person_c[r][c]; memset(person_c,false,sizeof(person_c));
        
        person_g[person_i][person_j] = 1;
        person_c[person_i][person_j] = true;
        
        queue<pair<int,int>> person_q;
        person_q.push(make_pair(person_i,person_j));
        
        while(!person_q.empty()){
            int i = person_q.front().first;
            int j = person_q.front().second;
            person_q.pop();
            
            for(int k=0; k<4; k++){
                int ni = i+dx[k];
                int nj = j+dy[k];
                
                if( 0<= ni and ni < r and 0<= nj and nj < c){
                    
                    //방문한 적이 없구!
                    //벽이 아니고
                    //fire_g[][]가  -1이 아니고!
                    //fire_g[][]보다 숫자가 낮으면! 지나갈 수 있따.
//                    cout << ni << nj << ' ' << endl;
                    if(person_c[ni][nj] == false
                       and g[ni][nj] != '#'
                       and (fire_g[ni][nj] == -1
                       or person_g[i][j] < fire_g[ni][nj])){
                        
//                        cout << "!!" << endl;
                        
                        person_c[ni][nj] = true;
                        person_g[ni][nj] = person_g[i][j] +1;
                        person_q.push(make_pair(ni,nj));
                        
                        
                    }
                        
                }
            }
            
        }
//        cout << "사람" <<endl;
//        for(int i=0; i<r; i++){
//            for(int j=0; j<c; j++){
//                if(person_g[i][j]==-1){
//                    cout << "-" << ' ';
//                }else{
//                    cout << person_g[i][j] << ' ';
//                }
//            }
//            cout << endl;
//        }
//        cout << endl;
        
        
        bool check_done = false;
        int ans = 10000000;
        for(int i =0; i<r; i++){
            for(int j=0; j<c; j++){
                if( i == 0 or i== r-1 or j==0 or j==c-1 ){ //가장자리만 체크!
                    if(person_g[i][j]!=-1){
                        check_done = true;
                        ans = min(ans, person_g[i][j]);
                    }
                }
            }
        }
        if(check_done==true){
            cout << ans<<endl;
        }else{
            cout << "IMPOSSIBLE" <<endl;
        }
    }
    return 0;
}
