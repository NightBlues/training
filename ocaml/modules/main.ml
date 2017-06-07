let () =
  let module Mya = Transport.Make (struct include A end) in
  let module Mya2 = Transport.Make (struct include A end) in
  Mya.init "qwe" "rty";
  Mya.show ();
  Mya2.init "zxc" "vbn";
  Mya2.show ();
  Mya.change "hey";
  Mya.show ()
  
     
