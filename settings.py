from checkEnv import checkEnv

domain_dir = "./dlc/data/"

yaml_base = checkEnv()

repo_base = "./dlc"

skip_ad_entries = False

cn_to_domestic = True

categories = {
    "select": ["geolocation-!cn, github"],
    "Social": ["discord", "reddit", "facebook", "google", "instagram", "twitter", "snapchat", "messenger"],
    "Speedtest": ["ookla-speedtest"],
    "Youtube": ["youtube", "vimeo"],
    "Spotify": ["spotify"],
    "Porn": ["category-porn"],
    "Apple": ["apple"],
    "Microsoft": ["microsoft"],
    "PayPal": ["paypal"],
    "Telegram": ["telegram", "signal"],
    "Netflix": ["netflix", "hulu", "showtimeanytime", "hbo"],
    "GlobalTV": [],
    "Steam": ["steam"],
    "AdBlock": [],
    "Domestic": ["geolocation-cn"]
}
