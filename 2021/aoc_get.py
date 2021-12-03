from requests import get
from datetime import date

def get_input(day=None, year=None, raw_format=False):
    today = date.today()
    cur_year = today.strftime('%Y')

    if not day:
        day = today.strftime('%d')
    
    if not year:
        year = cur_year
    
    inp = None
    file_name = 'input' + str(year) + '-' + str(day) + '.txt'

    if not(int(year) in range(2015, int(cur_year) + 1) and\
            int(day) in range(1, 26)):
        bad_time_msg = 'your date is ILLEGAL. You want to ruin Christmas?'
        print(bad_time_msg)
    else:
        try:
            f = open(file_name)
            inp = f.read()
        except FileNotFoundError:
            inp = get_some_input(day, year, raw_format)
            if inp.startswith("Please don't repeatedly request this endpoint"):
                print("ok seriously? trying to steal unreleased puzzles?")
                inp = None
            elif inp:
                save_forever(inp, file_name)
        except IOError:
            print('I/O error my friend')
    if not inp:
        print("You can't even get an input? Do you hate Christmas?")
        exit() # yes this is breaking single-exit principle, sorry

    return inp

def save_forever(inp: str, file_name: str):
    try:
        f = open(file_name, 'w')
        f.write(inp)
    except:
        print("can't write file. Merry Christmas.")
    return

def get_some_input(d: int, y: int, raw_format: bool) -> str:
    cookies = {'session': get_cookie()[:-1]}
    base_url = 'https://adventofcode.com/'
    url = base_url + str(y) + '/day/' + str(int(d)) + '/input'
    
    print(url)
    inp = None
    try:
        raw_input = get(url=url, cookies=cookies).content
        if raw_format == False:
            inp = raw_input.decode()
        else:
            inp = raw_input.decode('unicode_escape')
        inp = inp[:-1]
    except ConnectionError:
        print('could not connect to the internetics')
    except HTTPError:
        print('problem with HTTP response')
    except Timeout:
        print('request timed out')
    except:
        print('mysterious connexion problem')
        
    return inp


def get_raw_input(d, y):
    return get_some_input(d, y, False)

def get_reg_input(d, y):
    return get_some_input(d, y, True)

def get_cookie():
    try:
        f = open('../cookie.txt', 'r')
        cookie = f.read()
    except:
        print('No cookies, no gifts. Santa won\'t put up with this.')
        exit()
    return cookie
