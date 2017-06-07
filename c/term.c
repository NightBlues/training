#include <stdio.h>
#include <pty.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  int amaster = 0, aslave = 0;
  char * path = malloc(255);
  if(openpty(&amaster, &aslave, path, NULL, NULL) == -1) {
    printf("Could not open pty\n");
    exit(1);
  }
  printf("%s\n", path);
  /* close(0); */
  /* close(1); */
  /* close(2); */
  /* close(aslave); */
  /* dup2(amaster, 0); */
  /* dup2(amaster, 1); */
  /* dup2(amaster, 2); */
  /* char * argv[] = { "/bin/bash" }; */
  /* char * env[] = { NULL }; */
  /* execve("/bin/bash", argv, env); */
  while(1) {
    char buf[10];
    int len = read(amaster, &buf, 9);
    write(1, buf, len);
    len = read(0, &buf, 9);
    write(amaster, buf, len);
  }
  
  return 0;
}
