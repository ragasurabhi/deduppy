# deduppy
  * Start here: `run.sh`
  * `input.txt` is the input file
  * dedup.py reads from stdin and prints to stdout. Change the regex inside as needed

## Approach 2
```
cat input.txt | ./dedup2.py

```

## Approach 1
```
$ ./run.sh
+ cat input.txt
+ sort -k2 -t,
+ cat junk1.del
+ ./dedup.py
```
