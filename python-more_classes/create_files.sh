#!/bin/bash

for file in 0-rectangle.py 1-rectangle.py 2-rectangle.py 3-rectangle.py 4-rectangle.py 5-rectangle.py 6-rectangle.py 7-rectangle.py 8-rectangle.py 9-rectangle.py 101-nqueens.py
do
    echo "#!/usr/bin/python3" > $file
done

