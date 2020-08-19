default_settings = '''\
from checkEnv import checkEnv

domain_dir = "./dlc/data/"

yaml_base = checkEnv()

repo_base = "./dlc"

skip_ad_entries = False

cn_to_domestic = True

categories = {
    "Amazon": ["amazon"],
    "Apple": ["apple"],
    "BBC": ["category-media"],
    "GlobalTV": [],
    "Microsoft": ["microsoft"],
    "Netflix": ["hbo", "hulu", "netflix", "showtimeanytime"],
    "PayPal": ["paypal"],
    "Porn": ["category-porn"],
    "select": ["geolocation-!cn", "github"],
    "Social": ["discord", "facebook", "google", "instagram", "messenger", "reddit", "snapchat", "twitter", "whatsapp"],
    "Speedtest": ["ookla-speedtest"],
    "Spotify": ["spotify"],
    "Steam": ["steam"],
    "Telegram": ["signal", "telegram"],
    "Youtube": ["vimeo", "youtube"],
    "AdBlock": [],
    "Domestic": ["geolocation-cn"]
}
'''
