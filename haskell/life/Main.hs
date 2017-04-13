module Main(main) where

import qualified Graphics.Gloss as Gloss

window = Gloss.InWindow "Nice window" (600, 500) (350, 150)
drawing = Gloss.pictures [
  Gloss.color (Gloss.light Gloss.red) $ Gloss.circle 80,
  Gloss.translate 50 0 $ Gloss.color Gloss.green $ Gloss.circleSolid 30]


data World = World { size :: Int, lifes :: [Int] }


get_color 0 =
  Gloss.color (Gloss.greyN 0.8)
get_color 1 =
  Gloss.color (Gloss.greyN 0.2)


int_to_square :: Int -> Int -> (Int, Int) -> Gloss.Picture
int_to_square total size (alive, pos) =
  let mult_x = fromIntegral(pos `mod` size - size `div` 2)
      mult_y = fromIntegral(pos `div` size - (total `div` size `div` 2))
  in
    Gloss.translate (mult_x * 30) (mult_y * (-30))
    $ get_color alive
    $ Gloss.rectangleSolid 20 20


-- draw_world world =
--   case world of
--     World {size = size, lifes = lifes} ->
--       Gloss.pictures (map (int_to_square size) (zip lifes [1..]))
draw_world world =
  let int_to_square_s = int_to_square ((length . lifes) world)
                        (size world)
      enumed_lifes = (zip (lifes world) [0, 1..])
  in
    Gloss.pictures (map int_to_square_s enumed_lifes)


init_world = [0, 0, 0, 0, 0,
              0, 0, 0, 0, 0,
              0, 0, 1, 0, 0,
              0, 0, 0, 1, 0,
              0, 1, 1, 1, 0]


main = Gloss.play window Gloss.white 2
       (World { size = 5, lifes = init_world })
       draw_world
       (\ event world -> world)
       (\ time world -> world)




