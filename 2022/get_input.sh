day=$(date +'%-d')

# get input for current day
curl https://adventofcode.com/2022/day/$day/input -b "session=$(cat cookie)" > input_$day.txt
