rm c-vars.c
rm int
rm float
python3 genvars.py 20
gcc c-int.c -o int
gcc c-float.c -o float