
calc x y =
  case (x, y) of
    (True, True) -> True
    (True, False) -> True
    (False, True) -> True
    _ -> False

myconst = let x = 123 in x

main =
  print (calc True False)
  >>
  print myconst
