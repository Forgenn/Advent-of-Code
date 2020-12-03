#include <stdio.h>
#include <string.h>

int main(){

char vector[800][800],vector1[800][800];
int i=0,e=0;
  FILE *ptr;
  ptr =fopen("Day 2.txt","r");

 while (fgets(&vector[e],100,ptr) !=NULL){
      strcpy(&vector1[e][1],&vector[e]);
        i++;

      }
printf("\n%s\n",&vector1[0][1]);
    }
