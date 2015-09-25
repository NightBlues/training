(load "test.lisp")
(save-lisp-and-die "test" :toplevel (lambda () (main *posix-argv*)) :executable t)
