
type t = {
    a: string;
    b: string;
  }

let create a b = {a; b}

let show me = Printf.sprintf "{a=%s; b=%s}" me.a me.b

let myfunc me a =
  match !me with
  | Some me_val -> me := Some {me_val with a = a}; ()
  | None -> ()
