#!/bin/sh
echo "make sure you are in \"testing\" branch"
read null
git checkout master
git merge testing
git push origin master
git checkout testing
