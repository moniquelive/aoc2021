import Data.Char (digitToInt)

toDecimal :: [Int] -> Int
toDecimal [] = 0
toDecimal (x : xs) = x * 2 ^ length xs + toDecimal xs

reduce keep lst col
  | length lst == 1 = lst
  | otherwise =
    let ones = length [l !! col | l <- lst, l !! col == 1]
        zeros = length lst - ones
        delta = ones - zeros
     in filter (\line -> line !! col /= keep delta) lst

main = do
  file <- readFile "input-03.txt"
  let ll = map (map digitToInt) . lines $ file
  let ndigits = length (head ll)
  let halfLines = length ll `div` 2
  let epsilon =
        [ fromEnum ((length [l !! col | l <- ll, l !! col == 1]) >= halfLines)
          | col <- [0 .. ndigits -1]
        ]
  let gamma = [1 - x | x <- epsilon]

  putStrLn $ "part1: " ++ show (toDecimal epsilon * toDecimal gamma)

  let keep delta
        | delta > 0 = 1
        | delta < 0 = 0
        | otherwise = 1
  let invKeep = (1 -) . keep

  let oxygen = foldl (reduce keep) ll [0 .. ndigits -1]
  let co2 = foldl (reduce invKeep) ll [0 .. ndigits -1]

  putStrLn $ "part2: " ++ show ((toDecimal . head $ oxygen) * (toDecimal . head $ co2))
