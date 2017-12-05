#!/bin/bash
cd poll
read -p "Enter The current week (according to the AP): "  week
echo "Let's get week $week data!"
python getpoll.py $week
echo "got the poll"
cp ap2017/week${week}temp.csv ap2017/week${week}.csv
python getgames.py $week
echo "got the games"
python outputtop25.py $week
cat helloworld.txt ../../triplelog/ncaaf/base/ap-poll-base.js > ../../triplelog/ncaaf/ap-poll.js 
echo "done!"