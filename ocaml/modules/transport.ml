
module type Impl_iface = sig
  type t
  val create: string -> string -> t
  val myfunc: t option ref -> string -> unit
  val show: t -> string
end

module type Iface = sig
  val init: string -> string -> unit
  val change: string -> unit
  val show: unit -> unit
end

module Make (T : Impl_iface ) : Iface = struct
  let value = ref None
  let init a b = value := Some (T.create a b)
  let change a = T.myfunc value a
  let show () = match !value with
    | None -> print_endline "empty"
    | Some value -> print_endline @@ T.show value
end
