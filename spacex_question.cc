
#include<stdio.h>

int main() {
int b=5;
b = printf("Quiz On");
printf(" ");
printf("%d", b);
return 0;
}


#include <iostream>
using namespace std;
int main() {
       char arr[11] = "Hello world";
       cout << arr;
       return 0;
}



#include <stdio.h>
void main()
{
       static int x;
       if (x++ < 2)
       {
            main();
            printf(" Hey ");
     }

}


#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}