module type Interface = sig
  val method_a : int -> int
end

module Impl1 : Interface = struct
  let method_a x = x + 1
end

module Impl2 : Interface = struct
  let method_a x = x * 2
end
                             
let objects =
  [(module Impl1: Interface); (module Impl2: Interface)]

let () =
  let action m =
    let module M = (val m: Interface) in
    print_int @@ M.method_a 2    
  in
  List.iter action objects
