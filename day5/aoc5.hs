import System.IO  
import Control.Monad
import Data.List

main = do 
    contents <- readFile "input4.txt"
    let input =  (lines contents)
    let ids = getIDs input
    -- part 1
    print $ maximum $ ids
    -- part 2
    print $ head [x | x <- ([0..986] \\ ids), not (x `elem` ids), x+1 `elem` ids, x-1 `elem` ids]
    -- alt


halve :: [a] -> Int -> [a] 
halve xs a | a==0 = take s xs 
           | a==1 = drop s xs
    where
        s = (length xs) `div` 2

getIDs :: [String] -> [Int]
getIDs xs = [navigate x [0..127] [0..7] | x <- xs]


navigate :: [Char] -> [Int] -> [Int] -> Int
navigate [] (r:[]) (c:[]) = r*8+c
-- columns
navigate ('L':coms) x cols = navigate coms x ((halve cols 0))
navigate ('R':coms) x cols = navigate coms x ((halve cols 1))
-- rows
navigate ('F':coms) rows x = navigate coms ((halve rows 0)) x
navigate ('B':coms) rows x = navigate coms ((halve rows 1)) x
 