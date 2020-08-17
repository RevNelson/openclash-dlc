import os

routerBase = "/etc/openclash/rule_provider/"


def checkEnv():
    if os.path.isdir(routerBase):
        return routerBase
    else:
        output = "./output/"

        # Make output directory if it doesn't exist
        if not os.path.isdir(output):
            os.mkdir(output)

        return output
