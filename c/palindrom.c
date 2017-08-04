#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_palindrome(char *, int);

int main(int argc, char ** argv) {
  if(argc < 2) {
    printf("Usage: %s <string>\n", argv[0]);
    exit(1);
  }
  char * string_to_test = malloc(500);
  strcpy(string_to_test, argv[1]);
  if(is_palindrome(string_to_test, strlen(string_to_test)) == 0) {
    printf("palindrome\n");
  } else {
    printf("not a palindrome\n");
  }
}


int is_palindrome(char * string_to_test, int size) {
  for(int i=0; i < size / 2; i++) {
    char left = string_to_test[i];
    char right = string_to_test[size - i - 1];
    if(left != right) {
      return 1;
    }
  }
  return 0;
}
