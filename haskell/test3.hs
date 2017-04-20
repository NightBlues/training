-- use -fwarn-incomplete-patterns

data MyT = One | Two

instance Show MyT where
  show One = "One"
  show Two = "Two"

show2 One = "-1-"


main =
  print One >> print Two
  >> print (show2 One)
  >> print (show2 Two)
