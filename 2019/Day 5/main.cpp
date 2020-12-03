#include <fstream>
#include <sstream>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ifstream input;
    input.open("input.txt");
    long int verb=0,noun=0, parameter1,parameter2, parameter3, opcode;
    vector<int> dades;
    dades.reserve(100);
    string s,a;
    char t=',';



        getline(input,s);
    stringstream ss(s);

    while(getline(ss,a,t)){

        dades.push_back(stol(a));
    }



    for(size_t i=0; i < dades.size();i=i+4){
        opcode = dades[i] % 10;
        
        if(opcode == 1)
        {
            dades[dades[i+3]]=dades[dades[i+1]] + dades[dades[i+2]];
        } else if (opcode == 2)
            {
                dades[dades[i+3]]=dades[dades[i+1]] * dades[dades[i+2]];
            } else if (opcode == 3) 
                {
                    cout <<endl << "Input: ";
                    cin >> dades[dades[i+1]];
                    i = i-2;
                } else if (opcode == 4){
                    cout <<endl <<  "Parametre output: " << dades[dades[i+1]];
                    i = i - 2;
                } else if (opcode == 99){
                    break;
                }
    }

std::cout << "Resultat 2=" << 100*noun+verb << endl;
std::cout << "Noun" << noun << "Verb" << verb;
cout << endl << "Resultat 1: " << dades[0];
}