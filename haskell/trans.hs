import Data.Maybe
import Control.Monad
import Control.Monad.Trans.Maybe
-- import Control.Monad.Trans.Class
import Control.Applicative

-- parse :: (Monad (t IO), MonadTrans t, Alternative (t IO)) => t IO Int
parse :: MaybeT IO Int
parse = do
  x <- lift getLine
  guard $ foldl (\ a c -> a && c `elem` ['0'..'9']) True x
  return (read x :: Int)


actionInner :: MaybeT IO String
actionInner = do
  v <- parse
  let v2 = v * 2
  let v3 = show v2
  return v3

action :: MaybeT IO String -> IO String
action x = fromMaybe "" `liftM` runMaybeT x
-- action x = fromMaybe "" <$> runMaybeT x


main = action actionInner
