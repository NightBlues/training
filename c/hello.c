#include <stdio.h>


int main(int argc, char *argv[]) {
	char *name = "world";
	if(argc > 1) {
		name = argv[1];
	}
	printf("Hello, %s!\n", name);

	return 0;
}
