//
//  main.cpp
//  example_28_2206_bfs
//
//  Created by 조진영 on 25/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

char g[1002][1002];
int n; int m;

int di[]={0,0,1,-1};
int dj[]={1,-1,0,0};

int main(int argc, const char * argv[]) {
    
    cin >> n >> m;

    for(int i=0; i<n; i++){
        cin >> g[i];
    }

//    for(int i=0; i<n; i++){
//        for(int j=0; j<m; j++){
//            cout <<g[i][j];
//        }
//        cout << endl;
//    }
    
    ///////// !!
    int p[1002][1002][2];
    memset(p,0,sizeof(p));
    
    
    
    queue<vector<int>> q;
    q.push({0,0,0});
    p[0][0][0] = 1;
    p[0][0][1] = 1;
    
    while(!q.empty()){
        int i = q.front()[0];
        int j = q.front()[1];
        int z = q.front()[2];
        q.pop();
        for(int k=0; k<4; k++){
            int ni = i+di[k];
            int nj = j+dj[k];
            
            if(0<= ni and ni<n and 0<= nj and nj<m){
                
                //벽 안뚫었을때
                if(z==0){
                    //안뚫고
                    if(g[ni][nj] == '0' and p[ni][nj][z] == 0){
                        p[ni][nj][z] = p[i][j][z] + 1;
                        q.push({ni,nj,z});
                    }
                    //뚫고
                    if(g[ni][nj]=='1' and p[ni][nj][z+1] == 0){
                        p[ni][nj][z+1] = p[i][j][z] + 1;
                        q.push({ni,nj,z+1});
                    }
                    
                }else if(z==1){
                    if(g[ni][nj] == '0' and p[ni][nj][1] == 0){
                        p[ni][nj][z] = p[i][j][z] + 1;
                        q.push({ni,nj,z});
                    }
                }
            }
        }
    }
    
    if(p[n-1][m-1][0] == 0 and p[n-1][m-1][1] == 0){
        cout << -1 << endl;
    }else if(p[n-1][m-1][0] == 0){
        cout << p[n-1][m-1][1] << endl;
    }else if(p[n-1][m-1][1] == 0){
        cout << p[n-1][m-1][0] << endl;
    }else{
        cout << min(p[n-1][m-1][1] , p[n-1][m-1][0]) << endl;
    }
    
        
    
    
    return 0;
}
