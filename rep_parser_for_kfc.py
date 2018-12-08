import sc2reader
import os, sys

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

    #Ensure the rep is 1v1 and have at least 2 players
    if len(rep.teams) != 2 or rep.type != '1v1':
        return None

    if rep.winner == rep.teams[0]:
        loser = rep.teams[1]
    else:
        loser = rep.teams[0]

    winner_race = rep.winner.players[0].pick_race[0]
    loser_race = loser.players[0].pick_race[0]
    winner_id = rep.winner.players[0].name
    loser_id = loser.players[0].name
    length_string = length_format(rep.length.seconds)

    rep_name = '{}v{} {} (win) vs {} {}.SC2Replay'.format(winner_race, loser_race, winner_id, loser_id, length_string)
    return rep_name


if __name__ == '__main__':
    # Without extra arguments, the parser parses all replays in CURRENT directory. Else the parser parses all replays in 1st argument directory.
    if len(sys.argv) == 1:
        reps_path = os.curdir
    else:
        reps_path = sys.argv[1]

    reps  = list(filter(lambda f: os.path.isfile(os.path.join(reps_path, f)) and f.lower().endswith('.sc2replay'), os.listdir(reps_path)))

    for rep in reps:
        new_name = rep_new_name(os.path.join(reps_path, rep))
        if new_name is not None:
            os.rename(os.path.join(reps_path, rep), os.path.join(reps_path, new_name))
            print('{} has been renamed to {}.'.format(rep, new_name))
        else:
            print('{} is not a 1v1 game or does not at least contain 2 players.'.format(rep))