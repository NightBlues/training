let () = print_endline "Hello, js_of_ocaml!"


let rec fib = function
  | 0 -> 0
  | 1 -> 1
  | n when n > 1-> fib (n - 1) + fib (n - 2)
  | _ -> failwith "fib arg can't be negative"

let compose f g x = f @@ g x
let print = compose print_endline string_of_int

let () =
  print @@ fib 5;
  print @@ fib 1;
  print @@ fib 10

let () =
  Js.debugger ();
  print @@ fib (-1)
