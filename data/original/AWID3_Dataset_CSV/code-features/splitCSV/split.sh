#Change the relevant filename and execute in a terminal that is in the same directory with the relevant CSV file.
split_filter () { { head -n 1 Deauth2Selection.csv; cat; } > "$FILE"; }; export -f split_filter; tail -n +2 Deauth2Selection.csv | split --lines=50000 --filter=split_filter - split_
