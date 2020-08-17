from settings import skip_ad_entries, cn_to_domestic


def line_handler(line):
    parsed_line = ''
    if "full:" in line:
        parsed_line = "  - DOMAIN," + line.split("full:")[1]
    elif "keyword:" in line:
        parsed_line = "  - DOMAIN-KEYWORD," + line.split("keyword:")[1]
    elif "." not in line:
        parsed_line = "  - DOMAIN-KEYWORD," + line
    else:
        parsed_line = "  - DOMAIN-SUFFIX," + line
    return parsed_line


def parse_file(directory, domain):
    data = []
    domestic = []
    ads = []

    current_file = open(directory + domain, 'r')

    for line in current_file.readlines():
        # Check if we should skip ad entries
        skip_ad = skip_ad_entries & (" @ad" in line)

        # Skip comments, empty lines, and regex domains
        if (len(line) > 1) & ("#" not in line) & ("regex:" not in line) & (not skip_ad):
            # Get all includes
            if "include:" in line:
                parsed_data, parsed_domestic, parsed_ads = parse_file(
                    directory, line.strip().split("include:")[1])
                data.extend(parsed_data)
                domestic.extend(parsed_domestic)
                ads.extend(parsed_ads)
            # Separate domestic domains based on setting
            elif " @cn" in line:
                stripped_line = line_handler(line.strip().split(" @cn")[0])
                if cn_to_domestic:
                    domestic.append(stripped_line)
                else:
                    data.append(stripped_line)
            # Separate ad entries
            elif " @ads" in line:
                if not skip_ad_entries:
                    ads.append(line_handler(line.strip().split(" @ads")[0]))
            else:
                data.append(line_handler(line.strip()))

    return data, domestic, ads
