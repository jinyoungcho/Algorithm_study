//
//  main.cpp
//  example_51_5373
//
//  Created by 조진영 on 29/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N;
int M;
int MAP[51][51]; // 0~50
int main(int argc, const char * argv[]) {
    
    vector<pair<int,int>> house;
    vector<pair<int,int>> chicken;
    vector<bool> choose;
    
    cin >> N >> M;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> MAP[i][j];
            if(MAP[i][j]==2){
                chicken.push_back(make_pair(i,j));
            }else if(MAP[i][j]==1){
                house.push_back(make_pair(i,j));
            }
        }
    }
    
    // 3  // 3
    for(int i=0; i<M; i++){
        choose.push_back(true);
    }
    for(int i=0; i<chicken.size()-M; i++){
        choose.push_back(false);
    }
    
    sort(choose.begin(), choose.end());
    
    int ans = 100000000;
    
    do{
        vector<pair<int,int>> cho_chi;
        for(int i=0; i<choose.size(); i++){
            if (choose[i] == true){
                cho_chi.push_back(chicken[i]);
            }
        }
        
//        for(int i = 0; i<cho_chi.size(); i++){
//            cout << cho_chi[i].first << cho_chi[i].second << '-';
//        }cout << endl;
        
        vector<int> distance;
        
        for(int i=0; i<house.size(); i++){
            int sample_dis = 100000000;
            
            for(int j=0; j<cho_chi.size(); j++){
                int temp = abs(house[i].first-cho_chi[j].first) + abs(house[i].second-cho_chi[j].second);
                
                sample_dis = min(sample_dis, temp);
            }
            distance.push_back(sample_dis);
        }
        
        int temp_distance = 0;
        for(int i =0; i<distance.size();i++){
            temp_distance += distance[i];
        }
        
        ans = min(ans, temp_distance);
    }while(next_permutation(choose.begin(),choose.end()));
    
    cout << ans << endl;
    return 0;
}
