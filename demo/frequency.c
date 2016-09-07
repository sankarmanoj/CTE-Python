#include<stdio.h> //printf
#include<string.h>    //strlen
int main()
{
  char input[1000];

  printf("Enter Input :");
  fgets(input,1000,stdin);

  int size = strlen(input);

  for(int i = 0; i< size;i++)
    input[i]=tolower(input[i]);

  int index, maximum;
  int frequency[26];
  for(int i = 0; i< size; i++)
  {
    char x = input[i];
    if(x>='a'&&x<='z')
    frequency[x-'a']++;
  }
  char sortedArray [26];
  int count = 0;
  for(int i = 0; i< size;i++)
    {
      maximum = 0; index = -1;
      for(int j = 0; j< size; j++)
        {
          if (frequency[j]>maximum)
          {
            maximum = frequency[j];
            index = j;
          }
        }
        if(index!=-1)
        {
          sortedArray[count]=index+'a';
          frequency[index]=0;
          count++;
        }
  }
  for(int i = 0; i<26; i++)
  {
    if(isalpha(sortedArray[i]))
    printf("%c ",sortedArray[i]);
  }
  return 1;
}
