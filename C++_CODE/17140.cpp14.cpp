//
//  main.cpp
//  example_45_17140_samsung
//
//  Created by 조진영 on 26/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int A[101][101];
int r;
int c;
int kk;
int cnt[101];


int main(int argc, const char * argv[]) {
    // insert code here...

    cin >> r >> c >> kk;
    
    for(int i = 0; i<3; i++){
        for(int j=0; j<3; j++){
            cin >> A[i][j];
        }
    }
    
    int mr=3;
    int mc=3;
//    1 2 1 -> 1221
//    2 1 3 -> 211131
//    3 3 3
    
    
    
    int t = 0;
    while(t<101){
        if(A[r-1][c-1] == kk){
//            cout << r-1 <<" " << c-1 << " " << kk << endl;
            break;
        }
        
//        cout << mr << mc << "=" << endl;
        
        if(mr >= mc){
            int len_k=0;
            for(int i=0; i<mr; i++){
                // count!
                memset(cnt,0,sizeof(cnt));
                for(int j=0; j<mc; j++){
                    if(A[i][j] != 0){
                        cnt[A[i][j]]++;
                    }
                }
                // make new vec;
                vector<pair<int,int>> v;
                for(int j =1; j<101; j++){
                    if(cnt[j] != 0){ //0이 아니라면..!
                        v.push_back(make_pair(cnt[j],j));
                    }
                }
                sort(v.begin(), v.end());
                
                // resign A[][];
                for(int j=0; j<101; j++) A[i][j] = 0;
                
                int k = 0;
                for(int j=0; j<v.size(); j++){
                    A[i][k] = v[j].second;
                    A[i][k+1] = v[j].first;
                    k = k+2;
                }

                len_k = max(len_k,k);
            }
            mc = len_k;
            
//            for(int i=0; i<mr;i++){
//                for(int j=0; j<mc; j++){
//                    cout << A[i][j] << ' ';
//                }
//                cout << endl;
//            }
            
//            cout <<"mc: " << mc << endl;

        }else if(mr < mc){
            
            int len_k=0;
            for(int i=0; i<mc; i++){
                // count!
                memset(cnt,0,sizeof(cnt));
                for(int j=0; j<mr; j++){
                    if(A[j][i] != 0){
                        cnt[A[j][i]]++;
                    }
                }
                // make new vec;
                vector<pair<int,int>> v;
                for(int j =1; j<101; j++){
                    if(cnt[j] != 0){ //0이 아니라면..!
                        v.push_back(make_pair(cnt[j],j));
                    }
                }
                sort(v.begin(), v.end());
                
                // resign A[][];
                for(int j=0; j<101; j++) A[j][i] = 0;
                
                int k = 0;
                for(int j=0; j<v.size(); j++){
                    A[k][i] = v[j].second;
                    A[k+1][i] = v[j].first;
                    k = k+2;
                }
                
                len_k = max(len_k,k);
                

            }
            mr = len_k;
            
//            for(int i=0; i<mr;i++){
//                for(int j=0; j<mc; j++){
//                    cout << A[i][j] << ' ';
//                }
//                cout << endl;
//            }
        }
        
        
        t++;
    }
    
    
    if (t == 101){
        cout << -1 << endl;
    }else{
        cout << t << endl;
    }
    
    
    return 0;
}
