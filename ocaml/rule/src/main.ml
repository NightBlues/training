let parse fin =
  let lbuf = Lexing.from_channel fin in
  try
    Parser.main (Lexer.read) lbuf
    |> Expr.show |> print_endline
    (* |> Expr.eval |> print_endline *)
  with
  | Lexer.Error msg -> Printf.fprintf stderr "%s (at pos %d)\n" msg (Lexing.lexeme_start lbuf)
  | Parser.Error -> Printf.fprintf stderr "Syntax error at pos %d\n%!"
                                   (Lexing.lexeme_start lbuf)

let () =
  (* let user_input = (fun () -> if (read_int () = 1) then True else False) in *)
  (* let e = (And ((Call user_input), (Or (True, (And (True, False)))))) in *)
  (* print_endline (show_expr e); *)
  (* Printf.printf "%b\n" (reduce e) *)
  parse stdin
