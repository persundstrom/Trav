#!/bin/bash

file="$1"
head -1 $1 | sed 's/[^,]//g' | wc -c

