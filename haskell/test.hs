mysum [] = 0
mysum (a:t) = a + (mysum t)


main =
  getLine
  >>=
  (\ val -> return (read val::[Int]))
  >>=
  (\ list -> print (mysum list))
