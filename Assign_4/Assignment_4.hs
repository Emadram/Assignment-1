-- Problem 1: Get numbers divisible by 3
--TODO
-- ############ --
-- ############ --
-- ############ --
-- Problem 2: Get numbers divisible by 2
--TODO
-- ############ --
-- ############ --
-- ############ --
-- Problem 3: Count occurrences in a list
--TODO
-- ############ --
-- ############ --
-- ############ --
-- Problem 4: Triple all values in a list
--TODO
-- ############ --
-- ############ --
-- ############ --
-- Problem 5: Sort three numbers
--TODO
-- ############ --
-- ############ --
-- ############ --
-- Problem 6: Get a slice of the list
--TODO
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

-- ############ --
-- ############ --
-- ############ --
-- P02-Testing div_by_2:

-- ############ --
-- ############ --
-- ############ --
-- P03-Testing count:

-- ############ --
-- ############ --
-- ############ --
-- P04-Testing triple:

-- ############ --
-- ############ --
-- ############ --
-- P05-Testing sort:

-- ############ --
-- ############ --
-- ############ --
-- P06-Testing from_to:

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
