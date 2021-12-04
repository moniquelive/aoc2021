countGrowth :: [Int] -> Int
countGrowth n = length . filter (uncurry (<)) . zip n $ tail n

main = do
  file <- readFile "input-01.txt"

  let numbers = map read . words $ file
  putStr "parte 1: "
  print (countGrowth numbers)

  let numbers2 = zipWith3 (\x y z -> x + y + z) numbers (tail numbers) (tail . tail $ numbers)
  putStr "parte 2: "
  print (countGrowth numbers2)
