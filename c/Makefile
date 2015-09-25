FILES = hello forking

all: hello.c-lint forking.c-lint bin/hello bin/forking

bin/%: %.c dirs
	gcc -o ./$@ $<

%-lint:
	cpplint --filter=-whitespace/tab,-legal/copyright $$(echo $@ | sed -e "s/-lint//g")

clean:
	rm -rf ./bin

dirs:
	mkdir -p ./bin
