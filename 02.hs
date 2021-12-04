data Submarine = Submarine
  { hPos :: Int,
    depth :: Int,
    aim :: Int
  }
  deriving (Show)

toInt :: String -> Int
toInt = read

part1 :: Submarine -> [String] -> Submarine
part1 (Submarine hPos depth _) ("forward" : amt : _) = Submarine (hPos + toInt amt) depth 0
part1 (Submarine hPos depth _) ("down" : amt : _) = Submarine hPos (depth + toInt amt) 0
part1 (Submarine hPos depth _) ("up" : amt : _) = Submarine hPos (depth - toInt amt) 0
part1 sub _ = sub

part2 :: Submarine -> [String] -> Submarine
part2 (Submarine hPos depth aim) ("forward" : amt : _) = Submarine (hPos + toInt amt) (depth + toInt amt * aim) aim
part2 (Submarine hPos depth aim) ("down" : amt : _) = Submarine hPos depth (aim + toInt amt)
part2 (Submarine hPos depth aim) ("up" : amt : _) = Submarine hPos depth (aim - toInt amt)
part2 sub _ = sub

main = do
  file <- readFile "input-02.txt"
  let ll = map words . lines $ file
  let sub1 = foldl part1 (Submarine 0 0 0) ll
  let sub2 = foldl part2 (Submarine 0 0 0) ll

  putStrLn ("part 1: " ++ show (hPos sub1 * depth sub1))
  putStrLn ("part 2: " ++ show (hPos sub2 * depth sub2))
