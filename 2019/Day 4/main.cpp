#include <string>
#include <iostream>
#include <algorithm>
using namespace std;


int Part1(){
    int count=0;
        for(int i = 124075; i < 580769; i++)
    {
        bool adjacent=false;
        bool increase=true;

        string s=to_string(i);
        for(int j=0; j < s.size() - 1; j++)
        {

            if (s[j] == s[j+1])
                adjacent = true;

            if(s[j] > s[j+1])
                increase = false;

        }
    if (increase && adjacent){
        count++;
    }
       
    }
    return count;
}

int Part2(){
    int count=0;
        for(int i = 124075; i <= 580769; i++)
    {
        bool adjacent=false;
        bool increase=true;

        string s=to_string(i);
        for(int j=0; j < s.size() - 1; j++)
        {
            
            if (s[j] == s[j+1] && (s[j+2] != s[j]) && j < s.size() - 3 )  //Part 2 Falla
                adjacent = true;
            
            
            if(s[j] > s[j+1])
                increase = false;

        }
    if (increase && adjacent){
        count++;
    }
       
    }
    return count;
}

int main(){
    bool adjacent=false, increase=true;
    string Ant;

    cout << endl << "Part 1: " << Part1();
    cout << endl << "Part 2: " << Part2();
}