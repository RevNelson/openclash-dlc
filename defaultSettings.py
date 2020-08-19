default_settings = '''\
from checkEnv import checkEnv

domain_dir = "./dlc/data/"

yaml_base = checkEnv()

repo_base = "./dlc"

skip_ad_entries = False

cn_to_domestic = True

categories = {
    "Domestic": ["geolocation-cn"],
    "Microsoft": ["microsoft"],
    "select": ["geolocation-!cn", "github"]
}
'''
