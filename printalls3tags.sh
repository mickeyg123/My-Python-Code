#!/bin/bash

for bucket in $(aws s3api list-buckets --output=json | jq -r .Buckets[].Name); do
    echo $bucket # 2>/dev/null;
    aws s3api get-bucket-tagging --bucket $bucket --output=json --no-cli-pager 2>/dev/null;
done
