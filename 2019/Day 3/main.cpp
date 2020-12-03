#include <sstream>
#include <string>
#include <iostream>
#include <cmath>
#include <fstream>
#include <bits/stdc++.h> 
using namespace std;


int Part2(vector<pair<int,int>> &Set1,vector<pair<int,int>> &Set2){
    int steps = -1;

    for (int i = 0; i < Set1.size(); i++)
    {
        for (int j = 0; j < Set2.size(); j++)
        {
            if (( i+j < steps || steps == -1 ) && Set1[i] == Set2[j]){
                steps = i + j;
            }
        }
    }
    return steps+2;
}

int main(){     //Codi asqueros en una sola funcio, necessito utilitzar mes classes (o funcions d'ajuda)
    ifstream input;
    string li,s;
    char t = ',';
    int e;
    pair<int,int> PosActual(0,0);
    vector<pair<int,int>> SetPosicions={},SetPosicions2={};
     vector<pair<int,int>>::iterator itA;
    vector<vector<pair<int,int>>> Final={};

    input.open("input.txt");

for(int j=0;j < 2;j++){
    
    getline(input,li);
    stringstream ss(li);

    while(getline(ss,s,t)){

        if (s.at(0) == 'D'){ //Down
            s.erase(0,1);
            e=stoi(s);
            for(int i=0;i < e;i++){
                PosActual.second--;
                SetPosicions.push_back(PosActual);
            }
        }

        if (s.at(0) == 'R'){ //Right
            s.erase(0,1);
            e=stoi(s);
             for(int i=0;i < e;i++){
                PosActual.first++;
                SetPosicions.push_back(PosActual);
            }
        }

        if (s.at(0) == 'L'){ //Left
            s.erase(0,1);
            e=stoi(s);
             for(int i=0;i < e;i++){
                PosActual.first--;
                SetPosicions.push_back(PosActual);
            } 
        }

          if (s.at(0) == 'U'){ //Up
            s.erase(0,1);
            e=stoi(s);
             for(int i=0;i < e;i++){
                PosActual.second++;
                SetPosicions.push_back(PosActual);
            }
        }
    }
    Final.push_back(SetPosicions);
    SetPosicions.clear();
    PosActual.first=0;
    PosActual.second=0;

}
int minimum=-1, min=-1;


for(auto x : Final[0]){
    if((itA = find(Final[1].begin(),Final[1].end(),x)) != Final[1].end()){
        int dist = abs(x.first) + abs(x.second);


            if(minimum == -1 || dist < minimum){
                minimum = dist;
            }

    }
}

    cout << endl << "Part 1: " << minimum;
    cout << endl << "Part 2: " << Part2(Final[0],Final[1]);
}