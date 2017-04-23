module World (create_world, tick_world, size, lifes) where
import Debug.Trace
import Text.Printf


data World = World { size :: Int, lifes :: [Int] }

create_world size lifes = World {size = size, lifes = lifes}

get_neighbours_count world i = iter 0 0 (lifes world)
  where
    indexes = [i + 1, i - 1, up, upleft, upright, down, downleft, downright]
      where
        size_ = size world
        get_up = ((i `div` size_) - 1)
        get_up_ = if get_up == -1 then (((length . lifes) world) `div` size_) - 1
                  else get_up
        up = (get_up_ * size_) + (i `mod` size_)
        upleft = up - 1
        upright = up + 1
        get_down = ((i `div` size_) + 1)
        get_down_ = if get_down == ((length . lifes) world) `div` size_
                    then 0 else get_down
        down = (get_down_ * size_)  + (i `mod` size_)
        downleft = down - 1
        downright = down + 1
    -- iter acc i list | length list == 0 = (trace (show acc)) acc
    iter acc i [] = (trace (show indexes)) acc
    iter acc i (hd:tl) = iter acc_ (i + 1) tl
      where
        acc_ = acc + increment
        increment = (if alive_cond then 1 else 0)
        alive_cond = index_found && hd > 0
        index_found = length (filter (\ idx -> idx == i) indexes) > 0
          

tick_world time world =
  -- (trace (show time))
  World { size = (size world), lifes = new_lifes }
  where
    new_lifes = reverse (iter [] 0 world)
    iter acc i world | i == length (lifes world) = acc
    iter acc i world =
      case get_neighbours_count world i of
        2 -> iter (1:acc) (i + 1) world
        3 -> iter (1:acc) (i + 1) world
        x -> iter (0:acc) (i + 1) world
