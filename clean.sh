#!/bin/env bash
cd images
for f in *; do
    if [[ -d "$f" ]]; then
        cd $f

        rname=$(echo "$f" | sed -E 's/CWE[0-9]+_//')
        echo $rname
        mv $f $rname
        # find "$f" \! -type d -exec mv {} "$f/" \;
        find "$f" -empty -type d -delete
        # mv $f {$f//CWE[0-9]+_/}  
    fi    
done

cd ..
