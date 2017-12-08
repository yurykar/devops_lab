import requests
import getpass
import argparse
import datetime
import calendar


parser = argparse.ArgumentParser(prog='pr-stats', description='Cool program! Help to get info about pull requests!')
parser.add_argument('-v', '--version', help='Print version of programm', action='version', version='version 1.0')
parser.add_argument('-m', '--rate', help='Basic statistics about merged/closed rate', action='store_true')
parser.add_argument('-d', '--days_opened', help='Number of days opened', action='store_true')
parser.add_argument('-c', '--comments', help='Number of comments created', action='store_true')
parser.add_argument('-w', '--d_w_opened', help='Day of week opened', action='store_true')
parser.add_argument('-x', '--d_w_closed', help='Day of week closed', action='store_true')
parser.add_argument('-l', '--l_added', help='Number of lines added', action='store_true')
parser.add_argument('-z', '--l_deleted', help='Number of lines deleted', action='store_true')
parser.add_argument('-k', '--w_opened', help='Week opened', action='store_true')
parser.add_argument('-u', '--user', type=str, required=True, default='alenaPy', help='git username')
parser.add_argument('-r', '--repo', type=str, required=True, default='devops_lab', help='git repo')

args = parser.parse_args()
user = args.user
repo = args.repo


def cr_url(*elements):
    if len(elements) == 3:
        url_f_s = 'https://api.github.com/repos/' + elements[0] + '/' + elements[1] + '/pulls/'+str(elements[2])
        return url_f_s
    else:
        url_f_s = 'https://api.github.com/repos/' + elements[0] + '/' + elements[1] + '/pulls?state=all'
        return url_f_s


def authorization():
    print("Input Credentials (password will not be echoed)")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    auth = (username, password)
    return auth


def json_file(url_s_f):
    auth = authorization()
    r = requests.get(url_s_f, auth=auth)
    results = r.json()
    while 'next' in r.links.keys():
        url_s_f = r.links['next']['url']
        r = requests.get(url_s_f, auth=auth)
        results = results + r.json()
    return results


def rate(results_f):
    merge = 1
    closed = 1
    for i in range(results_f[0]['number']):
        if results_f[i]['merged_at']:
            merge += 1
        if results_f[i]['state']:
            closed += 1
    print("Merged/closed rate: {0:1.2}".format(merge/closed))


def days(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    create_date = datetime.datetime.strptime(r.json()['created_at'][0:10], "%Y-%m-%d")
    days_opened = datetime.datetime.now().timetuple().tm_yday - create_date.timetuple().tm_yday
    if days_opened >= 0:
        print("Pull request was opened {0} days ago".format(days_opened))
    else:
        print("Pull request was opened more than {0} days ago".format(datetime.datetime.now().timetuple().tm_yday))


def read(results_s_f):
    pl = int(input("Input the number of pull request: from 1 to {0} :".format(results_s_f[0]['number'])))
    return pl


def comments(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    print(r.json()['comments'])


def d_w_opened(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    create_date = datetime.datetime.strptime(r.json()['created_at'][0:10], "%Y-%m-%d")
    day_of_week = calendar.day_name[create_date.weekday()]
    print("Pull request was opened on {0}".format(day_of_week))


def d_w_closed(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    if r.json()['state'] == "open":
        print("The pull request is still open")
    else:
        close_date = datetime.datetime.strptime(r.json()['closed_at'][0:10], "%Y-%m-%d")
        day_of_week = calendar.day_name[close_date.weekday()]
        print("Pull request was closed on {0}".format(day_of_week))


def l_added(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    print(r.json()['additions'])


def l_deleted(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    print(r.json()['deletions'])


def w_opened(pl_num_f):
    auth = authorization()
    url_s_f = cr_url(user, repo, pl_num_f)
    r = requests.get(url_s_f, auth=auth)
    create_date = datetime.datetime.strptime(r.json()['created_at'][0:10], "%Y-%m-%d")
    number_week = create_date.isocalendar()[1]
    print("Pull request was opened on {0} week".format(number_week))


if args.rate:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    rate(result_s)
elif args.days_opened:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    days(pl_num)
elif args.comments:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    comments(pl_num)
elif args.d_w_opened:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    d_w_opened(pl_num)
elif args.d_w_closed:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    d_w_closed(pl_num)
elif args.l_added:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    l_added(pl_num)
elif args.l_deleted:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    l_deleted(pl_num)
elif args.w_opened:
    url_f = cr_url(user, repo)
    result_s = json_file(url_f)
    pl_num = read(result_s)
    w_opened(pl_num)



