#!/bin/bash

build_cmd() {
    newstr=()
    for cnt in $* ;do
        [ "${cnt:0:1}" == '$' ] && cnt=${cnt:1} && cnt=${!cnt}
        newstr+=($cnt)
    done
    echo "${newstr[*]}"
}

success=1
test_expected() {
    for f in test-data/*.fa; do
        coords=$f-coordinates
        expected=$f-get-subseqs-expected
        local cmd=$(build_cmd $1)
        if ! cmp -s <(eval $cmd) $expected; then
            echo "$cmd did not produce the expected output"
            diff <(eval $cmd) $expected
            echo
            success=0
        fi
    done
}

echo "Providing coordinates in a file"
test_expected './get-subseqs $f $coords'

echo "Providing coordinates on stdin"
test_expected 'cat $coords | ./get-subseqs $f'

echo "Providing coordinates as '-' (stdin)"
test_expected 'cat $coords | ./get-subseqs $f -'

if (( success == 1 )); then
    echo "Success."
else
    exit 2
fi
