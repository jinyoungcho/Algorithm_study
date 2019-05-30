//
//  main.cpp
//  example_47_17144
//
//  Created by 조진영 on 28/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int A[51][51];
int R;
int C;

bool check[51][51];

int di[] = {0,0,1,-1};
int dj[] = {1,-1,0,0};

int T;


void run_other_clock(int ci, int cj){
    deque<int> q;
    q.push_back(0);
    for(int j=1; j<C; j++){
        q.push_back(A[ci][j]);
        A[ci][j] = q.front();
        q.pop_front();
    }
    for(int i=ci-1; i>=0; i--){
        q.push_back(A[i][C-1]);
        A[i][C-1] = q.front();
        q.pop_front();
    }
    for(int j=C-2; j>=0; j--){
        q.push_back(A[0][j]);
        A[0][j] = q.front();
        q.pop_front();
    }
    for(int i=1; i<ci; i++){
        q.push_back(A[i][0]);
        A[i][0] = q.front();
        q.pop_front();
    }
}

void run_clock(int ci, int cj){
    deque<int> q;
    q.push_back(0);
    for(int j=1; j<C; j++){
        q.push_back(A[ci][j]);
        A[ci][j] = q.front();
        q.pop_front();
    }
    
    for(int i=ci+1; i<R; i++){
        q.push_back(A[i][C-1]);
        A[i][C-1] = q.front();
        q.pop_front();
    }

    for(int j=C-2; j>=0; j--){
        q.push_back(A[R-1][j]);
        A[R-1][j] = q.front();
        q.pop_front();
    }

    for(int i=R-2; i>ci; i--){
        q.push_back(A[i][0]);
        A[i][0] = q.front();
        q.pop_front();
    }
}

int main(int argc, const char * argv[]) {
    
    cin >> R >> C >> T;
    
    vector<pair<int ,int>> cleaner;
    
    memset(check, false, sizeof(check));
    
    for(int i = 0; i<R; i++){
        for(int j=0; j<C; j++){
            cin >> A[i][j];
            if (A[i][j] == -1){
                cleaner.push_back(make_pair(i,j));
            }
        }
    }
    
    
    for(int t = 0; t <T; t++){
        int AA[51][51];
        int B[51][51];
        for(int i = 0; i<R; i++){
            for (int j =0; j<C; j++){
                AA[i][j] = A[i][j];
                B[i][j] = 0;
            }
        }
        for(int i =0; i<R; i++){
            for(int j=0; j<C; j++){
                //해당 칸에 미세먼지가 있다면;
                if(A[i][j] > 0){
                    int num_dir=0;
                    bool check_dir[4] = {false, false,false,false};
                    for(int k = 0; k<4; k++){
                        int ni = i + di[k];
                        int nj = j + dj[k];
                        //4방향;
                        if(0<= ni and ni<R and 0<= nj and nj < C){
                            //청소기 없다면;
                            if(A[ni][nj] != -1){
                                check_dir[k] = true;
                                B[ni][nj] += A[i][j]/5; //확산 됨!
                            }
                        }
                    }
                    for(int z = 0; z<4; z++){
                        if(check_dir[z] == true){
                            num_dir++;
                        }
                    }
                    if(A[i][j] != 1){
                        AA[i][j] = A[i][j] - ((A[i][j]/5) * num_dir);
                    }
                }
            }
        }
        for(int i = 0; i<R; i++){
            for (int j =0; j<C; j++){
                A[i][j] = AA[i][j] + B[i][j];
            }
        }
        
        //////// 청소기 구현
        
        //반시계
        //step1;
        int ci = cleaner[0].first;
        int cj = cleaner[0].second;
        run_other_clock(ci,cj);
        
        //시계
        int ci2 = cleaner[1].first;
        int cj2 = cleaner[1].second;
        run_clock(ci2,cj2);
    }
    int ans = 0;
    for(int i =0; i<R; i++){
        for(int j =0; j<C; j++){
            if(A[i][j] > 0){
                ans += A[i][j];
            }
        }
    }
    cout << ans << endl;
    
    
    
    return 0;
}
