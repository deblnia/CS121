#!/bin/bash

echo "Getting files..."

wget -nv -O pa3.tgz https://www.classes.cs.uchicago.edu/archive/2019/fall/30121-1/pa3.tgz

echo "Unbundling files..."

tar -xzf pa3.tgz

rm pa3.tgz



