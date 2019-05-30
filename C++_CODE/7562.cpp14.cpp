//
//  main.cpp
//  example_24_7562_bfs
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[] ={-2,-1,1,2,-2,-1,1,2};
int dy[] ={1,2,2,1,-1,-2,-2,-1};

int T;




int bfs(int start_i, int start_j, int end_i, int end_j, int l){
    
    int g[301][301];
    bool c[301][301];
    
    for(int i=0; i<l; i++){
        for(int j=0; j<l; j++){
            g[i][j] = 0;
            c[i][j] = false;
        }
    }
    queue<vector<int>> q;
    q.push({start_i, start_j});
    c[start_i][start_j] = true;
    
    while(!q.empty()){
        int x = q.front()[0];
        int y = q.front()[1];
//        cout << x << y <<endl;
        q.pop();
        
        for(int i=0; i<8; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            
            if(0 <= nx and nx < l and 0 <= ny and ny <l){
                if(c[nx][ny] == false){
                    c[nx][ny] = true;
                    g[nx][ny] = g[x][y] + 1;
                    q.push({nx,ny});
                }
            }
        }
    }
    
//    cout << endl;
//    for(int i =0; i<l; i++){
//        for(int j=0; j<l; j++){
//            cout << g[i][j];
//        }
//        cout << endl;
//    }
    
    return g[end_i][end_j];
}

int main(int argc, const char * argv[]) {
    // insert code here...
    cin >> T;
    
    while(T--){
        int l;
        cin >> l;
        

        
        int start[2];
        int end[2];
        
        cin >> start[0] >> start[1];
        cin >> end[0] >> end[1];
        
        
        
        int ans = bfs(start[0], start[1], end[0], end[1], l);
        
        cout << ans <<endl;
    }
    
    return 0;
}
