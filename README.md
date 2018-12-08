# sc2RepTools
Tools to manage and analyse Starcraft II replays. Still in developing.

## Simple Rep Manager
**Rep_parser_for_kfc** is a simple rep managing tool developed for Kung Fu Cup series using **Python3**. It renames all Starcraft II replays under the same directory according to match-ups, players and winners, map name, and game length. For example, *'Blueshift LE (123).SC2Replay'* may be renamed to *'PvZ Player1 (winner) vs Player2 Blueshift 1h33min05s.SC2Replay'*. Note that this process is **NOT** recursive, it can only rename the replays **directly** under the directory.

Two types of files are provided: an [.exe](https://github.com/Oneoeigh/sc2RepTools/blob/master/bin/rep_parser_for_kfc.exe) file to run in Windows without python environment, and a [.py](https://github.com/Oneoeigh/sc2RepTools/blob/master/script/rep_parser_for_kfc.py) script.

### How to run rep_parser_for_kfc.py?

Put it under a directory and run it without arguments. It can rename all replays under the same directory. Example:
```
mv rep_parser_for_kfc.py the_directory
python3 rep_parser_for_kfc.py
```

Or run it with argument. It will use the first argument as the working directory. Example:
```
python3 rep_parser_for_kfc.py the_directory
```

### How to run rep_parser_for_kfc.exe?
Put the file under the replays directory. Double click rep_parser_for_kfc.exe, and all replays under the same directory will be renamed. 

Similar to the script version, it can also run with arguments where the first argument is considered as the working directory, using cmd.

### Future views

* An error log to analyze the reasons of failures.
* Increase efficiency.
* and more...
