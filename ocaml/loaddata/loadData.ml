let parse string =
  (* not implented as in haskell *)
  9, 2.3

let loadData fn =
  let fin = open_in fn in
  let rec loop acc =
    try
      let value = input_line fin
                  |> String.map (function ',' -> '.' | c -> c)
                  |> parse in
      loop (value :: acc)
    with End_of_file ->
      close_in fin;
      acc
  in
  loop []

let print_data data =
  List.map (fun (i,f) -> Printf.sprintf "%d -> %f\n" i f) data |>
    String.concat "" |> print_endline
  
let () =
  print_data (loadData "loadData.ml")
