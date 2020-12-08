
import Data.Text
import System.IO  
import Control.Monad
import Data.List

main = do 
    contents <- readFile "input4.txt"
    let input =  (lines contents)
    -- part 1
    print $ [ | x <- input ]


getbags :: [String] -> [String] -> [String] 
getbags init (x:xs) bags bagsprev = getbags init xs ([]++bags)
getbags inputinit input bags bagsprev = getbags
