{-# LANGUAGE OverloadedStrings #-}

import Data.List
import qualified Data.Map as M
import qualified Data.Map.Strict as SM
import qualified Data.Text as T

type Vector = (Int, Int)

type Plane = M.Map Vector Int

main = do
  -- parse
  contents <- readFile "input-05.txt"
  let ll =
        map (map (vec . T.splitOn ",") . T.splitOn " -> " . T.pack) . lines $
          contents

  -- partition
  let (straights, diags) =
        partition
          (\[(x1, y1), (x2, y2)] -> x1 == x2 || y1 == y2)
          ll

  -- declare parts
  let part1 = foldl fld M.empty straights
  let part2 = foldl fld part1 diags

  -- print parts
  putStrLn $ "part 1: " ++ (show . length . filter (> 1) . M.elems $ part1)
  putStrLn $ "part 2: " ++ (show . length . filter (> 1) . M.elems $ part2)
  where
    vec :: [T.Text] -> Vector
    vec [s, t] =
      ( read . T.unpack $ s,
        read . T.unpack $ t
      )
    vec _ = error "vec"

    fld :: Plane -> [Vector] -> Plane
    fld m [(x1, y1), (x2, y2)] =
      let coords (x1, y1) (x2, y2)
            | x1 == x2 && y1 < y2 = zip (repeat x1) [y1 .. y2]
            | x1 == x2 && y1 > y2 = zip (repeat x1) [y1, y1 -1 .. y2]
            | x1 < x2 && y1 == y2 = zip [x1 .. x2] (repeat y1)
            | x1 > x2 && y1 == y2 = zip [x1, x1 -1 .. x2] (repeat y1)
            | x1 < x2 && y1 < y2 = zip [x1 .. x2] [y1 .. y2]
            | x1 < x2 && y1 > y2 = zip [x1 .. x2] [y1, y1 -1 .. y2]
            | x1 > x2 && y1 < y2 = zip [x1, x1 -1 .. x2] [y1 .. y2]
            | x1 > x2 && y1 > y2 = zip [x1, x1 -1 .. x2] [y1, y1 -1 .. y2]
            | otherwise = error $ "coords " ++ show ((x1, y1), (x2, y2))
       in foldl
            (\m (x, y) -> SM.insertWith (+) (x, y) 1 m)
            m
            (coords (x1, y1) (x2, y2))
    fld _ _ = error "fld"
