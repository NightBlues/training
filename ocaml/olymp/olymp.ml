let read_line () =
  try
    Some (read_line ())
  with End_of_file -> None

let read_lines () =
  let rec loop acc =
    match read_line () with
    | None -> List.rev acc
    | Some line -> loop (line::acc)
  in loop []

let cut_r s =
  let stop =
    try String.index s '\r' with Not_found ->
      try String.index s '\n' with Not_found ->
        String.length s
  in
  (String.sub s 0 stop) ^ "\n"
          
let get_pair line =
  match String.split_on_char ' ' line with
  | [prefix; suffix] -> (prefix, cut_r suffix)
  | _ -> failwith "Invalid input"

let unzip pairs =
  let p, s = List.fold_left (fun (ltl, rtl) (left, right) -> (left::ltl, right::rtl)) ([], []) pairs in
  (List.rev p, List.rev s)

let () =
  let lines = read_lines () in
  let lines = List.map get_pair lines in
  let prefixes, suffixes = unzip lines in
  let buf_size = 160000 in
  let buf = Buffer.create buf_size in
  let show prefix suffix =
    if Buffer.length buf > buf_size - 10 then
      (Buffer.output_buffer stdout buf; Buffer.clear buf);
    Buffer.add_string buf prefix;
    Buffer.add_string buf suffix
  in
  List.iter (fun p -> List.iter (show p) suffixes) prefixes;
  Buffer.output_buffer stdout buf

            
