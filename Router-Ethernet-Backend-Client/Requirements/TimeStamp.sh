#!/bin/bash

while read line; do
  echo $line "|" $(date '+%Y-%m-%d %H:%M:%S.%6N');    
done