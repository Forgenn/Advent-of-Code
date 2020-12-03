#include <fstream>
#include <cmath>
#include <vector>
#include <iostream>
using namespace std;


int calcula(int x,ifstream& dada,int sum){
    
    x = x/3;
    x=floor(x);
    x=x-2;


        if(x > 0){
            sum=sum+x;
            return calcula(x,dada,sum);
        }
return sum;
}

int main(){
    ifstream dada;
    dada.open("iD2P2-VeryBigBoy");
    int sum=0,x=0,sumpar=0;
    vector<int> vec;
    while(dada >> x){
        int i=0;
        sumpar = sumpar + calcula(x,dada,sum);

     }
    cout << sumpar;
    return 0;
}

