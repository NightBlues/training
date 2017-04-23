module Draw(draw_world, int_to_square) where 
import qualified Graphics.Gloss as Gloss
import qualified World (lifes, size)

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
  let int_to_square_s = int_to_square ((length . World.lifes) world)
                        (World.size world)
      enumed_lifes = (zip (World.lifes world) [0, 1..])
  in
    Gloss.pictures (map int_to_square_s enumed_lifes)
