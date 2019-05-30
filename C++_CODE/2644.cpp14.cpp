//
//  main.cpp
//  example_22_2644_bfs
//
//  Created by 조진영 on 22/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <vector>
#include <queue>

using namespace std;


int n,s,e,T;

int g[100][100];
bool c[100];
int temp[100];
int main(int argc, const char * argv[]) {

    cin >> n;
    
    cin >> s >> e;
    
    cin >>T;
    
    while(T--){
        int i, j;
        cin >> i >> j;

        g[i][j] = 1;
        g[j][i] = 1;
    }
    
    
//    cout << endl;
//    for(int i = 0; i<=n;i++){
//        for(int j=0; j<=n;j++){
//            cout << g[i][j] << ',';
//        }
//        cout << endl;
//    }
    
    for(int i=1; i<=n;i++){
        c[i] = false;
        temp[i] = -1;
    }
    
    
    queue<int> q;
    q.push(s);
    c[s] = true;
    temp[s] = 0;
    
    while (!q.empty()){
        int new_s = q.front();
        q.pop();
//        cout << new_s<< endl;;
        for(int i=1; i<=n; i++){
            //연결 가능하다면!
//            cout << g[new_s][i]<<endl;
            if (g[new_s][i] >0 and c[i] == false){
//                cout << i << "!!";
                temp[i] = temp[new_s] + 1;
                c[i] = true;
                
                q.push(i);
            }
        }
    }
    
//    cout << endl;
//    for(int i = 1; i<=n;i++){
//        for(int j=1; j<=n;j++){
//            cout << g[i][j] << ',';
//        }
//        cout << endl;
//    }
    
//    cout << endl;
    cout << temp[e] <<endl;
    return 0;
}


