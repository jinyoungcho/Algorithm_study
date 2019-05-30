//
//  main.cpp
//  example_33_1039_bfs
//
//  Created by 조진영 on 26/04/2019.
//  Copyright © 2019 조진영. All rights reserved.
//

#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    string N;
    int K;
    cin >> N >> K;
    
    queue<string> q;
    q.push(N);
    
    while(K--){
        int qSize = q.size();
        set<string> found;
        
        for(int j=0; j<qSize; j++){
            string str = q.front();
            q.pop();
            
            if(found.count(str)==1){
                continue;
            }
            
            found.insert(str);
            
            for(int k=0; k<str.size()-1; k++){
                for(int l=k+1; l<str.size(); l++){
                    if(k>0 or str[l] != '0'){
                        swap(str[k],str[l]);
                        q.push(str);
                        swap(str[k], str[l]);
                    }
                }
            }
            
            
        }
        
    }
    
    string result="0";
    while(!q.empty()){
        result = max(result, q.front());
        q.pop();
    }
    if(result[0]=='0'){
        cout<< -1 << endl;
    }else{
        cout << result << endl;
    }
    
    return 0;
}
