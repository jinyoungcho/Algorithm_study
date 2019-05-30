//
//  main.cpp
//  example_23_2178_bfs
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <vector>
using namespace std;


int N,M;
char g[101][101];
int dx[4] ={0,0,1,-1};
int dy[4] ={1,-1,0,0};
int g2[101][101];
bool c[101][101];
int main(int argc, const char * argv[]) {

    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        cin >> g[i];
    }
    
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            g2[i][j] = -1;
            c[i][j] = false;
        }
    }

    queue<vector<int>> q;
    q.push({0,0});
    c[0][0] = true;
    g2[0][0] = 1;

    while(!q.empty()){
        int ix = q.front()[0];
        int jx = q.front()[1];
        q.pop();
        
        for(int i = 0; i<4; i++){
            int ni = ix + dx[i];
            int nj = jx + dy[i];
            
            //지나갈 수 있다 면! 그리고 지나간 적이 없다면!
            if (0 <= ni < N and 0 <= nj < M){
                
                if (g[ni][nj] == '1' and c[ni][nj]==false){
                    c[ni][nj] = true;
                    g2[ni][nj] = g2[ix][jx] + 1;
                    q.push({ni,nj});
                }
            }
            
        }
    }
    
    
    cout << g2[N-1][M-1] << endl;
    
//    for(int i=0; i<N; i++){
//        for(int j=0; j<M; j++){
//            cout << g2[i][j] <<'.';
//        }
//        cout<< endl;
//    }
//
    return 0;
}
