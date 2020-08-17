import os

from settings import domain_dir, yaml_base, categories, repo_base
from gitHandler import pull_repo
from parseFile import parse_file
from writeYAML import writeYAML

print(pull_repo())

print("Scanning for domains...")
entries = os.scandir(domain_dir)


def count_files(files):
    return len([1 for x in list(files) if x.is_file()])


print("Found " + str(count_files(entries)) + " domain files.")


category_count = 0

domain_count = 0

category_domains = ["payload:"]

domestic_domains = ["payload:"]

ad_domains = ["payload:"]


def append(list, entry):
    if len(entry) > 0:
        list.extend(entry)


for category in categories:
        # Skip empty categories
    if len(categories[category]) > 0:
        print("Finding domains in the {} category...".format(category))

        for domain in categories[category]:
            # Check for domain matches in category
            if os.path.isfile(domain_dir + domain):
                parsed_category_domains, parsed_domestic_domains, parsed_ad_domains = parse_file(
                    domain_dir, domain)

                if category == "Domestic":
                    append(domestic_domains, parsed_category_domains)
                    append(domestic_domains, parsed_domestic_domains)
                elif category == "AdBlock":
                    append(ad_domains, parsed_category_domains)
                    append(ad_domains, parsed_domestic_domains)
                else:
                    append(category_domains, parsed_category_domains)
                    append(domestic_domains, parsed_domestic_domains)

                append(ad_domains, parsed_ad_domains)

                # Add domain count
                domain_count += len(parsed_category_domains) + \
                    len(parsed_domestic_domains) + len(parsed_ad_domains)

        # Write the rule files
        # if category not in "Domestic AdBlock":
        writeYAML(yaml_base + category + ".yaml", category_domains)

        # Increase category_count
        category_count += 1

        # Reset category_domains
        category_domains = ["payload:"]

writeYAML(yaml_base + "Domestic" + ".yaml", domestic_domains)
writeYAML(yaml_base + "AdBlock" + ".yaml", ad_domains)

print("\nMade rules for {} domains in {} categories.\n".format(
    domain_count, category_count))
