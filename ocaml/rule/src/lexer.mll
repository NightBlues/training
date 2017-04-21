{
open Lexing

exception Error of string
}

let white = [' ' '\t' '\n']+
let ident = ['a'-'z']['a'-'z''0'-'9''_']+

rule read = parse
  | white { read lexbuf }
  | "(" { Parser.L_BRACKET }
  | ")" { Parser.R_BRACKET }
  | "True" { Parser.True }
  | "False" { Parser.False }
  | "and" { Parser.And }
  | "or" { Parser.Or }
  | "&&" { Parser.And_inf }
  | "||" { Parser.Or_inf }
(*  | ident { Parser.IDENT ident } *)
  | eof { Parser.EOF }
  | _ { raise (Error ("Unexpected char: " ^ Lexing.lexeme lexbuf)) }
