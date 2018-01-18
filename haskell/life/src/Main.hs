module Main(main) where

import qualified Graphics.Gloss as Gloss
import Draw (int_to_square, draw_world)
import World (create_world, tick_world)

window = Gloss.InWindow "Nice window" (600, 500) (350, 150)
-- drawing = Gloss.pictures [
--   Gloss.color (Gloss.light Gloss.red) $ Gloss.circle 80,
--   Gloss.translate 50 0 $ Gloss.color Gloss.green $ Gloss.circleSolid 30]


init_world = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


main :: IO ()
main = Gloss.play window Gloss.white 1
       (create_world 10 init_world)
       draw_world
       (\ event world -> world)
       tick_world




