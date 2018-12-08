import sc2reader
import os

# files = filter(os.path.isfile, os.listdir( os.curdir ))
# temporarily use list for ez test
files = list(filter(os.path.isfile, os.listdir(os.curdir))

replay = sc2reader.load_replay(fl[0], load_map=True)

replay.winner # as a team
# In [15]: replay.filename
# Out[15]: 'ºº∑Í∏Ææ» ∆˙ - ∑°¥ı (21).SC2Replay'

# In [16]: replay.release_string
# Out[16]: '4.7.1.70326'

# In [17]: replay.category
# Out[17]: 'Private'

# In [18]: replay.end_time
# Out[18]: datetime.datetime(2018, 12, 6, 11, 24, 12)

# In [19]: replay.type
# Out[19]: '1v1'

# In [20]: replay.map_name
# Out[20]: '세룰리안 폴 - 래더'

# In [21]: replay.game_length
# Out[21]: Length(0, 548)

# In [22]: replay.teams[0].players[0]
# Out[22]: Player 1 - Stats (Protoss)

# In [23]: replay.teams[1].players[0]
# Out[23]: Player 2 - llllllllllll (Terran)

# In [24]: replay.teams[1].players[0].name
# Out[24]: 'llllllllllll'

# In [25]: replay.teams[1].players[0].pick_race
# Out[25]: 'Terran'

# In [43]: replay.length.seconds
# Out[43]: 548

# In [45]: replay.winner
# Out[45]: Team 1: Player 1 - Stats (Protoss)