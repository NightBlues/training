open Lwt

external reraise : exn -> _ = "%reraise"
                                
let failfunc str =
  if true then
    [%lwt raise (Failure "smth went wrong...")]
  else
    return (str ^ ", sure")


let myf str =
  backtrace_bind (fun exn -> try Printf.printf "%s" __LOC__;reraise exn with exn -> exn)
                 (Lwt_unix.sleep 0.1)
                 (fun _ -> failfunc str)

(* let middlef str = *)
(*   myf str *)
(*   >>= fun s -> return (" = " ^ s ^ " = ") *)


(* let main2 () = *)
(*   let%lwt x = *)
(*     try%lwt *)
(*           middlef "asdf" *)
(*     with exn -> *)
(*       let msg = Printexc.to_string exn in *)
(*       Printf.printf "Error occured: %s\n" msg; *)
(*       fail exn *)
(*   in *)
(*   Printf.printf "%s\n" x; return_unit *)



let main2 () =
  backtrace_bind (fun exn -> try reraise exn with exn -> exn)
                 (myf "hey")
                 (fun x -> Printf.printf "%s\n" x; return_unit)

let main () =
  catch (fun () -> main2 ())     (fun e ->
       print_endline (Printexc.to_string e);
       print_string (Printexc.get_backtrace ());
       return ()
)

       


let () =
  Lwt_main.run (main ())
