#!/bin/sh

for dir in */; do
( cd "$dir" && python3 *.py ) 
done