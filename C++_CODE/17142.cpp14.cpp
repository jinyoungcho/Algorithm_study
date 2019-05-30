//
//  main.cpp
//  example_44_17142
//
//  Created by 조진영 on 26/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

int map[51][51];
int v_map[51][51];
int N;
int M;



int di[] = {0,0,1,-1};
int dj[] = {1,-1,0,0};

vector<pair<int,int>> vir_vec;

int main(int argc, const char * argv[]) {
    
    cin >> N >> M;
    
    memset(v_map,-1,sizeof(v_map));
    
    for(int i=0; i<N;i++){
        for(int j=0; j<N; j++){
            cin >> map[i][j];
            
            if(map[i][j]==2){
                vir_vec.push_back(make_pair(i,j));
            }else if(map[i][j]==1){
                v_map[i][j] = -2;
            }
        }
    }
    vector<int> v_vec; // 바이러스를 놓을수 있는 갯수만큼.
    
    for(int i=0; i<M; i++){ // 바이러스 갯수 만큼.
        v_vec.push_back(1);
    }
    for(int i=0; i<vir_vec.size() - M; i++){
        v_vec.push_back(0);
    }
    
    sort(v_vec.begin(), v_vec.end());

//    for(int i=0; i<v_vec.size(); i++){
//        if (v_vec[i] == 1){
//            cout << vir_vec[i].first << vir_vec[i].second;
//            cout << ",";
//        }
//    }
    
//    for(int i=0; i<N; i++){
//        for(int j=0; j<N; j++){
//            cout << v_map[i][j] << ' ';
//        }
//        cout << endl;
//    }
//    cout << endl;
    
    vector<int> answer_list;
    
    do{
        int temp_map[51][51];
        
        for(int i=0; i<51; i++){
            for(int j=0; j<51; j++){
                temp_map[i][j] = v_map[i][j];
            }
        }
        
        vector<pair<int,int>> temp_vir_list;
        
        for(int i=0; i<v_vec.size(); i++){
            if (v_vec[i] == 1){
//                cout << vir_vec[i].first << vir_vec[i].second;
//                cout << ",";
                temp_vir_list.push_back(vir_vec[i]);
            }
        }
//        cout << endl;
        
        queue<pair<int,int>> q;
        
        for(int i =0; i<temp_vir_list.size(); i++){
            temp_map[temp_vir_list[i].first][temp_vir_list[i].second] = 0;
            q.push(make_pair(temp_vir_list[i].first,temp_vir_list[i].second));
        }
        
//        cout <<"temp_map"<<endl;
//        for(int i=0; i<N; i++){
//            for(int j=0; j<N; j++){
//                cout << temp_map[i][j] << ' ';
//            }
//            cout << endl;
//        }
//        cout << endl;
        
        while(!q.empty()){
            int i= q.front().first;
            int j= q.front().second; q.pop();
            
//            cout << i << j << ',';
            
            for(int k=0; k<4; k++){
                int ni = i+di[k];
                int nj = j+dj[k];
                
                if(0 <= ni and ni<N and 0<= nj and nj<N){
                    // 벽이 아니고 -2, 방문한적이 없다면 -1!
                    if(temp_map[ni][nj] != -2 and temp_map[ni][nj] == -1){
                        temp_map[ni][nj] = temp_map[i][j] + 1;
                        q.push(make_pair(ni, nj));
                    }
                }
            }
        }
        
        
//        for(int i=0; i<N; i++){
//            for(int j=0; j<N; j++){
//                cout << temp_map[i][j] << ' ';
//            }
//            cout << endl;
//        }
//        cout << endl;
        
        
        int maxi = -10000000;
        int done = true;
        
        for(int i=0; i<vir_vec.size(); i++){
            temp_map[vir_vec[i].first][vir_vec[i].second]=0;
        }
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(temp_map[i][j] == -1){
                    done = false;
                }else if(temp_map[i][j] != -2){
                    maxi = max(maxi, temp_map[i][j]);
                }
            }
        }
        
        if(done == true){
            answer_list.push_back(maxi);
        }
        
    }while(next_permutation( v_vec.begin(), v_vec.end() ));
    
    int mini = 100000;

    if(answer_list.size() == 0){
        cout << -1 << endl;
    }else{
        for(int i=0; i<answer_list.size(); i++){
            mini = min(mini,answer_list[i]);
        }
        cout << mini << endl;
    }
    
    
    return 0;
}
