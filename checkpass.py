import requests
import hashlib
# import sys ~ ignore


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}"
                           f", check the api and try again cb")
    return res


def get_leaks(hashes, hash_for_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_for_check:
            return count

    return 0


def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first_five)

    return get_leaks(response, tail)


def main(args):
    password = args
    # for password in args:
    # print(password)
    count = pwned_api_check(password)
    if count:
        print(f"{password} was found {count} times")
    else:
        print(f"{password} was not found")
    print('finished')


if __name__ == '__main__':
    print('CAUTION - terminal input might be stored in terminal command history')
    code_to_check = input('Please enter password to check: ')

    main(code_to_check)
# CAUTION - terminal input might be stored in history
