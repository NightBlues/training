module My:Core.Monad.Basic = struct
  type 'a t = Value of 'a
  let return x = Value x
  let bind x ~f = match x with Value x -> f x
  let map = `Define_using_bind
end
                               
module MyM = Core.Monad.Make(My)


open MyM
let print_my x = print_endline @@ string_of_int x; return ()

let _ =
  return 123 >>= fun x -> return @@ x * 2 >>= print_my

let _ =
  (* open MyM.Let_syntax *)
  let open Let_syntax in
  let%bind x = return 123 in
  let%bind y = return @@ x * 2 in
  print_my y
