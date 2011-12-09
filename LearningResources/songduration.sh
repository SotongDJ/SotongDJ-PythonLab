## url: http://superuser.com/questions/231950/export-total-length-of-mp3-files-in-a-folder
## If you're working on Mac OS or any Unix system you can install ffmpeg and use the following command to extract the duration of a single file:
ffmpeg -i filename.mp3 2>&1 | egrep "Duration" | cut -d ' ' -f 4 | sed s/,//
## That would for example return "00:08:17.4".
## You can use this in a shell script of course, so for example this would list all of the mp3 files in a folder and their duration to the right.

#!/bin/bash
# call me with mp3length.sh directory
# e.g. ./mp3length . 
# or ./mp3length my-mp3-collection

for file in $1/*.mp3
do
    echo -ne $file "\t"
    ffmpeg -i "$file" 2>&1 | egrep "Duration"| cut -d ' ' -f 4 | sed s/,//
done


