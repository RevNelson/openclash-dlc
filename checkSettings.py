from os import path
from defaultSettings import default_settings

settings = './settings.py'

required_attributes = ["domain_dir", "yaml_base",
                       "skip_ad_entries", "cn_to_domestic", "categories"]


def check_attributes(attributes):
    import settings
    failed_attributes = []
    for attribute in attributes:
        if hasattr(settings, attribute):
            continue
        else:
            failed_attributes.append(attribute)
    if len(failed_attributes) > 0:
        return False, failed_attributes
    else:
        return True, []


def check_settings(counter=0):
    # Prevent loop if writing fails
    if counter > 3:
        print("Error writing settings.py file")
        return False

    # Check if settings file exists
    if path.isfile('./settings.py'):
        # Check if all required variables exist
        has_attributes, failed_attributes = check_attributes(
            required_attributes)
        if has_attributes:
            return True
        else:
            print(failed_attributes)
            for attribute in failed_attributes:
                print('{} not found in settings.py').format(attribute)
            return False
    else:
        # Make default settings file
        with open(settings, 'w') as f:
            f.write(default_settings)
            f.flush()
        return check_settings(counter + 1)
