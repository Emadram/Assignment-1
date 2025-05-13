-- Problem 1: Get numbers divisible by 3
div_by_3 :: [Int] -> [Int]
div_by_3 xs = [x | x <- xs, x `mod` 3 == 0]
-- ############ --
-- ############ --
-- ############ --
-- Problem 2: Get numbers divisible by 2
div_by_2 :: [Int] -> [Int]
div_by_2 [] = []  -- returns an empty list if empty
div_by_2 (x:xs)
    | x `mod` 2 == 0 = x : div_by_2 xs  -- divisible by 2, include it and recurse
    | otherwise      = div_by_2 xs      -- skip and recurse
-- ############ --
-- ############ --
-- ############ --
-- Problem 3: Count occurrences in a list
count :: Eq a => a -> [a] -> Int
count _ [] = 0 
count elem (x:xs)
    | elem == x  = 1 + count elem xs  
    | otherwise  = count elem xs      --just recurse
-- ############ --
-- ############ --
-- ############ --

-- Task 4: triple
-- Return a list where all values are triple the values in the original list.
-- Uses map with a helper function.
triple :: [Int] -> [Int]
triple xs = map tripleHelper xs

tripleHelper :: Int -> Int
tripleHelper x = x * 3
-- ############ --
-- ############ --
-- ############ --

-- Task 5: sort
-- Return the 3 input numbers in sorted order.
-- Must be non-recursive and use guards.
sort :: Ord a => a -> a -> a -> [a]
sort a b c
    | a <= b && b <= c = [a, b, c]
    | a <= c && c <= b = [a, c, b]
    | b <= a && a <= c = [b, a, c]
    | b <= c && c <= a = [b, c, a]
    | c <= a && a <= b = [c, a, b]
    | otherwise        = [c, b, a]
-- ############ --
-- ############ --
-- ############ --

-- Task 6: from_to
-- Return a slice of the list from position n to m (inclusive), using take and drop.
-- Note: Counting starts at 1.
from_to :: Int -> Int -> [a] -> [a]
from_to n m xs = take (m - n + 1) (drop (n - 1) xs)
-- ############ --
-- ############ --
-- ############ --

-- Problem 7: Get the nth element (recursively)
nth_element :: Int -> [a] -> a
nth_element 1 (x:_) = x
nth_element n (_:xs) = nth_element (n - 1) xs
nth_element _ [] = error "Indexing out of list bounds"
-- ############ --
-- ############ --
-- ############ --
-- Problem 8: Get the mth element (using library functions)
mth_element :: Int -> [a] -> a 
mth_element m list = head (drop (m - 1) list)
-- ############ --
-- ############ --
-- ############ --
-- Problem 9: Add corresponding elements from two lists
add_lists :: Num a => [a] -> [a] -> [a]
add_lists [] ys = ys  -- if first list is empty, return second list
add_lists xs [] = xs  -- if second list is empty, return first list
add_lists (x:xs) (y:ys) = (x + y) : add_lists xs ys  -- add heads, then recurse on tails
-- ############ --
-- ############ --
-- ############ --
-- Problem 10: Convert numeric grade to letter grade
classify :: (Ord a, Num a) => a -> Char
classify n
    | n >= 90   = 'A'  -- 90 or above gets an A
    | n >= 70   = 'B'  -- 70-89 gets a B
    | n >= 50   = 'C'  -- 50-69 gets a C
    | otherwise = 'D'  -- below 50 gets a D
-- ############ --
-- ############ --
-- ############ --
--TEST SECTION
main :: IO ()
main = do
-- p01-Testing div_by_3:
  putStrLn "Testing div_by_3:"
  print $ div_by_3 [6, 10, 15, 3, 9, 5]        -- numbers divisible by 3
  print $ div_by_3 [3, -6, 9, 11, -12]  --[3, -6, 9, -12]
-- ############ --
-- ############ --
-- ############ --
-- P02-Testing div_by_2:
  putStrLn "Testing div_by_2:"
  print $ div_by_2 [6, 12, 15, 3]
  print $ div_by_2 [3, -5, 4, -2, 8, -15]  --[-2, 4, 8]
-- ############ --
-- ############ --
-- ############ --
-- P03-Testing count:
  putStrLn "Testing count:"
  print $ count 'b' ['a', 'b', 'c', 'b', 's']  
  print $ count 3 [3, 5, 4, 2, 8, 15, 3]       
  print $ count 'x' ['a', 'b', 'c', 'b', 's']  
  print $ count (-3) [3, -3, -3, 5, 8] 
-- ############ --
-- ############ --
-- ############ --
  -- P04-Testing triple:
  putStrLn "Testing triple:"
  print $ triple [2, 4, 5, 1]        -- basic case: [6,12,15,3]
  print $ triple [0, -1, 3]         -- includes zero and negative: [0,-3,9]
  -- ############ --
  -- ############ --
  -- ############ --

  -- P05-Testing sort:
  putStrLn "Testing sort:"
  print $ sort 3 4 1                -- out of order: [1,3,4]
  print $ sort 10 5 7              -- another permutation: [5,7,10]
  print $ sort 1 1 1               -- all same: [1,1,1]
  -- ############ --
  -- ############ --
  -- ############ --

  -- P06-Testing from_to:
  putStrLn "Testing from_to:"
  print $ from_to 3 5 [4,3,6,5,8,7,2,0]  -- [6,5,8]
  print $ from_to 1 2 [9,8,7,6]         -- [9,8]
  print $ from_to 5 5 [1,2,3,4,99,100]  -- single element: [99]
  -- ############ --
  -- ############ --
  -- ############ --
-- P07-Testing nth_element:
  putStrLn "Testing nth_element:"
  print $ nth_element 3 [2, 5, 4, 6, 8]  -- get 4 case
--Only for test  print $ nth_element 10 [1, 2, 3]  -- error case
-- ############ --
-- ############ --
-- ############ --
-- P08-Testing mth_element:
  putStrLn "Testing mth_element:"
  print $ mth_element 3 [2, 5, 4, 6, 8]  -- get 4 case
  print $ mth_element 1 [99, 100, 101]  -- first element case
-- ############ --
-- ############ --
-- ############ --
-- P09-Testing add_lists:
  putStrLn "Testing add_lists:"
  print $ add_lists [3, 4, 5] [10, 20, 30]  -- get [13,24,35] case
  print $ add_lists [3, 4, 5] [10, 20, 30, 88, 42]  -- longer second list case
  print $ add_lists [3, 4, 5] [10]  -- shorter second list case
  print $ add_lists [] [1, 2, 3]  -- empty first list case
-- ############ --
-- ############ --
-- ############ --
-- P10-Testing classify:
  putStrLn "Testing classify:"
  print $ classify 87  -- get 'B' case 
  print $ classify 92  -- get 'A' case
  print $ classify 65  -- get 'C'
  print $ classify 45  -- get 'D' case
  print $ classify 70  -- edge/boundary case
