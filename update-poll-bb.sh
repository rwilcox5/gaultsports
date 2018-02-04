#!/bin/bash
cd poll-bb
read -p "Enter The current week (according to the AP): "  week
echo "Let's get week $week data!"
python getpoll.py $week
echo "got the poll"
cp ap1718/week${week}temp.csv ap1718/week${week}.csv


python getgames.py $week
echo "got the games"
python outputtop25.py $week


python rankedchoice.py $week

cat helloworld.txt helloworldRC.txt ../../triplelog/ncaab/base/ap-poll-base.js > ../../triplelog/ncaab/ap-poll.js 
echo "done!"