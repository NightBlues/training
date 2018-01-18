open Sexplib.Std
type t = Maybe of int | Nothing [@@deriving sexp]


let main () =
  (* print_endline @@ show @@ Maybe 1; *)
  print_endline @@ Sexplib.Sexp.to_string @@ sexp_of_t @@ Maybe 1
