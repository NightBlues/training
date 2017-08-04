(* loadData :: String *)
(*          -> IO [(Int, Double)] *)
(* loadData fn = *)
(*   do cnt <- readFile fn *)
(*      return $ *)
(*        map parse $ *)
(*        lines $ *)
(*        map (\c -> if c == ',' *)
(*                     then '.' *)
(*                     else c) cnt *)

let parse string =
  (* not implented as in haskell *)
  9, 2.3

let loadData fn =
  BatFile.lines_of fn
  |> BatEnum.map @@ String.map (function ',' -> '.' | c -> c)
  |> BatEnum.map parse


let () =
  (* force lazy list *)
  let data = loadData "Bat_loadData.ml" in
  BatEnum.iter (fun (i,f) -> Printf.printf "%d -> %f\n" i f) data
