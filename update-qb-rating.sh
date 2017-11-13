#!/bin/bash
cd nfl_scrape
python getqbstats.py
echo "got qb stats for 2017"
python genstr.py
cat helloworld.txt ../../gaultsports-site/nfl/base/custom-QB-rating-base.js > ../../gaultsports-site/nfl/custom-QB-rating.js


