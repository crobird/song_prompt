# song_prompt
Simple script to give some randomize beginnings for songmaking with a modular rack.
Given a file of newline separated modules, the script will return a BPM in a range and
one or more modules that help provide a starting point to new work.

## usage:
```
usage: song_prompt.py [-h] [--min MIN] [--max MAX] [--round] [-F MODULE_FILE]
                      [-N NUMBER_OF_MODULES]

optional arguments:
  -h, --help            show this help message and exit
  --min MIN             Minimum BPM range (default: 80)
  --max MAX             Maximum BPM range (default: 160)
  --round               Round BPM to nearest 5
  -F MODULE_FILE, --module_file MODULE_FILE
                        File of modules to randomize through (default:
                        modules.txt)
  -N NUMBER_OF_MODULES, --number_of_modules NUMBER_OF_MODULES
                        Number of modules to return (default: 1)
```
