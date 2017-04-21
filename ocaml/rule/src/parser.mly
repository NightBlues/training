%{
let build_tree constr exps =
  let rec build_tree_ acc = function
   | [] -> acc
   | hd::tl -> build_tree_ (constr (hd, acc)) tl
  in
  match exps with
  | e1::(e2::_ as tl) -> build_tree_ e1 tl
  | _ -> Expr.True (* never gets here *)
%}
%token True
%token False
%token And
%token Or
%token And_inf Or_inf
%token L_BRACKET R_BRACKET
%token <string> IDENT
%token EOF

%left And_infx Or_inf
%nonassoc And Or

%start <Expr.t> main

%%
main:
| e = expression EOF { e }
  
expression:
| e = func_call { e }
| L_BRACKET e=expression R_BRACKET { e }
| le=expression And_inf re=expression { Expr.And (le, re) }
| le=expression Or_inf re=expression { Expr.Or (le, re) }
| se = simple_expression { se }

simple_expression:
| True {Expr.True}
| False {Expr.False}
(* | id = IDENT { Expr.Ident id } *)

func_call:
 | And exps = many_expressions_rev {build_tree (fun (e1,e2) -> Expr.And (e1, e2)) exps}
 | Or exps = many_expressions_rev {build_tree (fun (e1,e2) -> Expr.Or (e1, e2)) exps}


(* many_expressions: l = many_expressions_rev { List.rev l } *)

many_expressions_rev:
 | e = expression e2 = expression { [e2; e] }
 | tl = many_expressions_rev e = expression { e :: tl }