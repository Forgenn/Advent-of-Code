#include <stdio.h>
#include <stdlib.h>



int main(){
  int vector[200000],vector1[200000],sum=0,i=0;
  FILE *ptr;
  ptr =fopen("Day 1.txt","r");

for(;;){
  while (fscanf(ptr,"%d",&vector[i]) !=EOF){
            sum = sum+vector[i];
            vector1[i]=sum;
            printf("%d\n",vector1[i] );

            for(int e=0;e < 1014;e++){
              for(int j=e+1;j < 1014;j++){
              printf("pasa \n");
              if (vector[e]==vector[j]){
                printf("%d acabat",vector[e] );
                return 0;
              }
            }
          }
            i++;
      }
      rewind(ptr);
    }
  }
