#include <stdio.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <pty.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char * argv[]) {
  char * path = argv[1];
  int term = open(path, O_NOCTTY | O_RDWR);
  while(1) {
    char buf[10];
    int len = read(0, &buf, 10);
    write(term, buf, len);
    len = read(term, buf, 10);
    write(1, buf, len);
  }
  
  return 0;
}
