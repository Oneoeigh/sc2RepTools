import sc2reader
import os, sys
import re
import progressbar

def length_format(seconds):
    h = seconds//3600
    m = (seconds - h * 3600)//60
    s = seconds - h * 3600 - m * 60
    length_string = ''
    if h > 0:
        length_string += str(h) + 'h'
    if m > 0:
        if h > 0 and m < 10:
            mm = '0' + str(m)
        else:
            mm = str(m)
        length_string += mm + 'min'
    if m > 0 and s < 10:
        ss = '0' + str(s)
    else:
        ss = str(s)
    length_string += ss + 's'
    return length_string


def rep_new_name(rep_old_name):
    rep = sc2reader.load_replay(rep_old_name, load_map=False, level=0)

    # Ensure the rep is 1v1 and contain exactly 2 players
    if len(rep.teams) != 2 or rep.type != '1v1' or len(rep.teams[0].players) != 1 or len(rep.teams[1].players) != 1:
        return None

    # The rep is not a tie:
    if rep.winner is not None:
        if rep.winner == rep.teams[0]:
            loser = rep.teams[1]
        else:
            loser = rep.teams[0]

        winner_race = rep.winner.players[0].pick_race[0]
        loser_race = loser.players[0].pick_race[0]
        winner_id = rep.winner.players[0].name
        loser_id = loser.players[0].name
        map_name = rep.map_name
        length_string = length_format(rep.length.seconds)

        rep_name = '{}v{} {} (win) vs {} {} {}.SC2Replay'.format(winner_race, loser_race, winner_id, loser_id, map_name, length_string)
    # The rep is a tie
    else:
        race1 = rep.teams[0].players[0].pick_race[0]
        race2 = rep.teams[1].players[0].pick_race[0]
        id1 = rep.teams[0].players[0].name
        id2 = rep.teams[1].players[0].name
        map_name = rep.map_name
        length_string = length_format(rep.length.seconds)

        rep_name = '{}v{} {} (draw) vs {} (draw) {} {}.SC2Replay'.format(race1, race2, id1, id2, map_name, length_string)
    return rep_name


def rep_re_name(old_name, new_name, old_name_set, new_name_set, reps_path):
    
    # Add the sequence number of replay names by 1.
    def add_name_number(name):
        pattern = r'\((\d+)\)'
        m = re.search(pattern, name)
        
        # When ther is no sequence number in the replay's name, add a (1) at the rear.
        # E.g. 'pvp 4min18s.SC2Replay' -> 'pvp 4min18s (1).SC2Replay'
        if m is None:
            split_name = name.split('.')
            name_with_num = split_name[0] + ' (1).'+ split_name[1]
        # When there is a sequence number, add 1 to the number.
        # E.g. 'pvp 4min18s (99).SC2Replay' -> 'pvp 4min18s (100).SC2Replay'
        else:
            name_with_num = re.sub(pattern, lambda m: '({})'.format(str(int(m.group(1)) + 1)), name)
        return name_with_num

    old_name_set.remove(old_name)
    while new_name in old_name_set or new_name in new_name_set:
        new_name = add_name_number(new_name)
    new_name_set.add(new_name)

    os.rename(os.path.join(reps_path, old_name), os.path.join(reps_path, new_name))

    return new_name


def rep_remame_indir(reps_path):
    reps  = set(filter(lambda f: os.path.isfile(os.path.join(reps_path, f)) and f.lower().endswith('.sc2replay'), os.listdir(reps_path)))
    rep_old_names = set(reps)
    rep_new_names = set()
    rep_failures = set()

    for rep in progressbar.progressbar(reps, redirect_stdout=True):
        try:
            new_name = rep_new_name(os.path.join(reps_path, rep))
            if new_name is not None:
                new_name = rep_re_name(rep, new_name, rep_old_names, rep_new_names, reps_path)
                print('{} has been renamed to {}.'.format(rep, new_name))
            else:
                print('{} is not a 1v1 game or does not contain exactly 2 players.'.format(rep))
        except Exception:
            rep_failures.add(rep)
            print('{} causes an internal exception. See more details in err log.'.format(rep))
            # TO BE DONE: maintain an error log

    # print fails
    if len(rep_failures) > 0:
        print('Fails in dealing with these reps:')
        for failure in rep_failures:
            print('    ' + failure)


if __name__ == '__main__':
    # Without extra arguments, the parser parses all replays in CURRENT directory. Else the parser parses all replays in 1st argument directory.
    if len(sys.argv) == 1:
        reps_path = os.curdir
    else:
        reps_path = sys.argv[1]

    rep_remame_indir(reps_path)

    # debug in windows
    input("Press Enter to continue...")
