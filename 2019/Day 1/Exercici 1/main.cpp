#include <fstream>
#include <cmath>
#include <iostream>
using namespace std;
int main(){
    ifstream dada;

    dada.open("input.txt");
    int sum=0,x;
    while(dada >> x){
        x = x/3;
        x=floor(x);
        x=x-2;
        sum=sum+x;
    }
    cout << sum;
    return 0;
}