
module type Iface = sig
  type t
  val string_of_t : t -> string
end

module A = struct
  type t = int
  let string_of_t value = Printf.sprintf "%d" value
end


module B = struct
  type t = float
  let string_of_t value = Printf.sprintf "%f" value
end


let create_and_print (type a) m_ value =
  let module M = (val m_: Iface with type t = a) in
  print_endline (M.string_of_t value)


let () =
  create_and_print (module B) 1.5;
  create_and_print (module A) 2;
