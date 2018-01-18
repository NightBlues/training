open Batteries

let lns = IO.lines_of IO.stdin |> Enum.map (String.split_on_char ' ') |> Array.of_enum
let ps = Array.map (fun (x::_) -> x) lns
let ss = Array.map (fun (_::x::_) -> x) lns

let () =
    ps |> Array.iter (fun p -> 
        ss |> Array.iter (fun s -> 
            IO.nwrite IO.stdout p; IO.write_line IO.stdout s ))
