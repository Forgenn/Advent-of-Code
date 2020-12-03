#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ifstream input;
    input.open("D2P2-RealisticBigBoy");
    long int verb=0,noun=0;
    vector<int> dades;
    dades.reserve(100);
    string s,a;
    char t=',';

    

for(int k=0;k <=99;k++){
    for(int j=0; j <= 99;j++){

        getline(input,s);
    stringstream ss(s);

    while(getline(ss,a,t)){

        dades.push_back(stol(a));
    }

        dades[1]=k;
        dades[2]=j;

    for(size_t i=0; i < dades.size();i=i+4){
        if(dades[i] == 1)
        {
            dades[dades[i+3]]=dades[dades[i+1]] + dades[dades[i+2]];
        } else if (dades[i] == 2)
            {
                dades[dades[i+3]]=dades[dades[i+1]] * dades[dades[i+2]];
            } else if (dades[i] == 99) 
                {
                    if(dades[0] == 19690720)
                    {
                    verb=dades[2];
                    noun=dades[1];
                    }
                    break;
                }
    }
    dades.clear();
    
    }
}

std::cout << "Resultat 2=" << 100*noun+verb << endl;
std::cout << "Noun" << noun << "Verb" << verb;
}