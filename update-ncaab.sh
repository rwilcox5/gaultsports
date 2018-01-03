cd ncaab
python getscores.py allgames
echo "got games"
python genjsfromscores.py
python makedab.py
echo "created rankings"
cat helloworld.txt ../../triplelog/ncaab/base/custom-NCAAB-rpi-base.js > ../../triplelog/ncaab/custom-NCAAB-rpi.js
cat hello_dab.txt ../../triplelog/ncaab/base/dab-base.js > ../../triplelog/ncaab/dab.js

