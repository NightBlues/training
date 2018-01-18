let myf () () =
  print_endline "myf"


let () =
  myf (print_endline "arg1") (print_endline "arg2")
