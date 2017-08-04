FILES = hello forking

all: hello.c-lint forking.c-lint bin/hello bin/forking bin/plus

bin/%: %.c dirs
	gcc -g -o ./$@ $<

bin/%: %.cpp dirs
	g++ -std=gnu++14 -o ./$@ $<

%-lint:
	cpplint --filter=-whitespace/tab,-legal/copyright $$(echo $@ | sed -e "s/-lint//g")

clean:
	rm -rf ./bin

dirs:
	mkdir -p ./bin
