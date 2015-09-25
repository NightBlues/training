#include <stdio.h>
#include <unistd.h>

#define log(x) printf("%s", x)
#define MAX_FORKS 100

pid_t pids[MAX_FORKS];
int pid_count = 0;

pid_t spawn_fork();

int main(int argc, char *argv[]) {
	pid_t p;
	int i;

	for(i = 9; i > 0; i--) {
		printf("\rYou have %d sec", i);
		fflush(stdout);
		sleep(1);
	}
	printf("\r\n");

	for(i = 0; i < 10; i++) {
		p = spawn_fork();
		printf("Spawned fork #%d, with pid=%d\n", i, p);
	}

	sleep(5);

	return 0;
}


pid_t spawn_fork() {
	if(pid_count >= MAX_FORKS) {
		log("Cloud not fork");
		return -1;
	}
	pid_count += 1;
	if((pids[pid_count-1] = fork()) < 0) {
		log("Cloud not fork");
	} else if (pids[pid_count-1] == 0) {
		sleep(10);
		printf("Hello from child #%d, with pid=%d\n", pid_count-1, pids[pid_count-1]);
		_exit(0);
	}

	return pids[pid_count-1];
}
