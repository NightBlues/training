type t = | True | False
         | Not of t
         | And of t * t
         | Or of t * t
         | Ident of string
         | Call of (unit -> t) [@@deriving show]


let rec reduce = function
  | True -> true
  | False -> false
  | Ident s -> true
  | Not e -> not (reduce e)
  | And (e1, e2) -> (reduce e1) && (reduce e2)
  | Or (e1, e2) -> (reduce e1) || (reduce e2)
  | Call f -> reduce (f ())


let eval e = Printf.sprintf "%b" (reduce e)
