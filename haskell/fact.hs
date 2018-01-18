module Main where

import Control.Monad
import Control.Parallel.Strategies
import Control.DeepSeq


fact 1 = 1
fact n = n * fact (n - 1)

-- fact n = foldl (*) 1 [x| x <- [1..n]]


main = do
  let nums = [149000, 150000, 151000, 152000] :: [Integer]
  -- let nums_calced = map fact nums
  -- let nums_calced = runEval $ forM nums (rpar . fact)
  let nums_calced = withStrategy (evalTraversable $ rpar . fact) nums
  -- let nums_calced = withStrategy strat nums
  --       where strat = (rseq (foldl (+) 0)) `dot` (evalTraversable $ rpar . fact)
  -- let nums_calced = withStrategy strat (foldl (+) 0 $ map fact nums)
  --       where strat = rseq `dot` (parList rseq)
  forM_ nums_calced print
  -- print nums_calced

