#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
 
using namespace std;
 
int word[200];
string str[52];
int ans;
 
void useAlphabet(int n, int k, char start)
{
    if (k < 0)
        return;
 
    if (k == 0)
    {
        int val = 0;
        for (int i = 0; i < n; i++)
        {
            int len = str[i].size();
            int cnt = 0;
            for (int j = 0; j < len; j++)
            {
                if (word[str[i][j]])
                    cnt++;
                else
                    break;
            }
            if (cnt == len)
                val++;
        }
 
        ans = max(ans, val);
 
        return;
    }
 
    for(int i = start; i <= 'z'; i++)
        if (!word[i])
        {
            if (k > 'z' - i + 1)
                continue;
            word[i] = true;
            useAlphabet(n, k - 1, i + 1);
            word[i] = false;
        }
}
int main()
{
    int n, k;
    cin >> n >> k;
 
    for (int i = 0; i < n; i++)
    {
        cin >> str[i];
        str[i].erase(str[i].begin(), str[i].begin() + 4);
        str[i].pop_back();
        str[i].pop_back();
        str[i].pop_back();
        str[i].pop_back();
    }
    
    word['a'] = true;
    word['c'] = true;
    word['i'] = true;
    word['n'] = true;
    word['t'] = true;
    useAlphabet(n, k - 5, 'a');
    
    cout << ans;
    
    return 0;
}

