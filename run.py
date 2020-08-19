from gitHandler import pull_this_repo, fetch_submodule, pull_dlc_repo

print(pull_this_repo())

print(fetch_submodule())

print(pull_dlc_repo())


def main():
    from checkSettings import check_settings

    if check_settings():
        from parseCategories import parse_categories
        parse_categories()


main()
