day=$(date +'%-d')
day=4

# get input for current day
curl https://adventofcode.com/2022/day/$day/input -b "session=$(cat cookie.txt)" > input_$day.txt
