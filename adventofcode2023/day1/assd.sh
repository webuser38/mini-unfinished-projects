#!/bin/bash

function value() {
    numbers=()
    for number in $1; do
        if [[ $number =~ ^[0-9]+$ ]]; then
            numbers_code+=($number)
        fi
    done

    local code_res=''
    code_res+=${numbers_code[0]}
    code_res+=${numbers_code[${#numbers_code[@]}-1]}
    code_res=$(($code_res))
    echo $code_res
}

end_result=0
while IFS= read -r line || [[ -n $line ]]; do
    end_result=$((end_result + $(value "$line")))
done < "codes.txt"

echo $end_result
