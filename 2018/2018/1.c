#include <stdio.h>
#include <stdlib.h>



int main(){
  int vector[20000],sum=0,i=0;
  FILE *ptr;
  ptr = fopen("Day 1.txt","r");

  while (fscanf(ptr,"%d",&vector[i]) !=EOF){
            sum = sum+vector[i];

            i++;
      }
      printf("%d",sum);
}
