# openclash-dlc
This script uses [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community) as a submodule. It:
* Pulls the latest commit from this repo.
* Pulls the latest commit from the community list.
* Verifies the `settings.py` file for errors.
	* If no `settings.py` file exists, one will be made with the default settings.
* Runs through each category in the `settings.py` file and looks for a match for the domain(s).
* Looks through the matched domain files in the community list and parses them line-by-line.
  *If an `include:` line is found, it will look for that file and parse it as well.
* Formats each line to match cases such as `DOMAIN`, `DOMAIN-SUFFIX`, and `DOMAIN-KEYWORD`.
* Generates one `.yaml` file for each category which includes all domains found for that domain.


The output is a `.yaml` file formatted as a classical `rule-provider` file as per the [clash documentation](https://lancellc.gitbook.io/clash/clash-config-file/rule-provider). The script will look for a folder at `/etc/openclash/rule_provider` (*the default location OpenClash looks for `rule-provider` files*). If found, the `.yaml` file(s) will be made in that folder. If not, the script will make a folder called `output` in the root of the git clone and save the .yaml files there. - e.g. `/path/to/clone/output/Domestic.yaml`


## Requirements
* SSH access to your OpenWRT device
* [`git`](https://openwrt.org/packages/pkgdata/git) and [`python3`]([https://openwrt.org/packages/pkgdata/python3](https://openwrt.org/packages/pkgdata/python3)) packages.
* [OpenClash](https://github.com/vernesong/OpenClash) installed and functioning.

## How to use
1. SSH into your OpenWRT device.
2. Clone this repo. - `git clone https://github.com/RevNelson/openclash-dlc.git`
3. Run the `run.py` script. - `python3 openclash-dlc/run.py`
	* Repeat this step anytime you change the `settings.py` file.
4. Check which Proxy Groups you have in the [Servers and Groups]([http://192.168.0.1/cgi-bin/luci/admin/services/open](http://10.0.10.1/cgi-bin/luci/admin/services/open)) tab inside OpenClash. 
	* You may need to change the IP address in that link to match your router
	* Add more groups as you see fit to break up the routing of various domains
5. Go to the [Rule Providers and Groups](http://10.0.10.1/cgi-bin/luci/admin/services/openclash/rule-providers-settings) tab inside OpenClash.
6. Under Custom Rule Providers and Groups, click the Add button.
	* Type in any Rule Providers Name you want
	* For Rule Providers Type, select `file`
	* For Rule Behavior, select `classical`
	* For Rule Providers Path, select the `.yaml` file you want for this rule (You will need one rule per file/category)
	* For Set Proxy Group, select any Proxy Group available in Step 3. Whichever group you choose will be the group that handles all domains in the `.yaml` file.
	* Click the `COMMIT CONFIGURATIONS` button.
7. Click the `APPLY CONFIGURATIONS` button.

## Considerations
The order of categories in the `settings.py` file does not matter. However, the order of the rules you add in Step 5 (under *Custom Rule Providers and Groups* in the *Rule Providers and Groups* tab) **does** matter. Rules higher in the list will supersede any below it. For example, the `microsoft` domain file has a line to include the `github` domains. Because many Microsoft services aren't blocked in a certain country, I would put those domains in Domestic. However, certain github repos may be blocked by a certain country, so I would want a specific rule for github domains placed higher within OpenClash so those domains are handled by the Proxy Group of my choice. You must click the `APPLY CONFIGURATIONS` button to save the order of the rules.
 
 All domains tagged with `@ads` will be moved to the `AdBlock` category (and resulting `AdBlock.yaml` file.
*The `skip_ad_entries` setting in `settings.py` can be changed to `True` if you don't want to include those domains in the resulting `AdBlock.yaml` file. This can be useful if you are using a different AdBlock solution like [Pi-Hole]([https://pi-hole.net/](https://pi-hole.net/)) for example. You can also simply ignore the `AdBlock.yaml` file in that case, and not add a rule for it within OpenClash.*

By default, all domains tagged with `@cn` will be moved to the `Domestic` category (and resulting `Domestic.yaml` file) instead of the category the script was parsing when it found the domain. You can disable this by setting `cn_to_domestic` to `False` in `settings.py`.

## Changing settings
After running `run.py` the first time, a `settings.py` file is created. Feel free to edit this file, or make your own file before running the script. Take note of the following required variables:
| Name |Type  |Description | Default |
|--|--|--|--|
|repo_base|string|Location for the [domain]||
| domain_dir|string|Location of domain files from the [domain-list-community](https://github.com/v2fly/domain-list-community) repo.|"./dlc/data/"|
|yaml_base|string|Full path for where the final `.yaml` files should be written to.|Return of the checkEnv() function. Checks to see if "/etc/openclash/rule_provider/" exists and returns that string if it does. If not, it creates an `output` folder and returns "./output/"|
|skip_ad_entries|Boolean|If `True`, any domains marked with `@ads` will be skipped.|False|
|cn_to_domestic|Boolean|If `True`, any domains marked with `@cn` will be added to the `Domestic` category instead of the category they were found in.|True|
|categories|Dictionary (values are lists of strings)|Categories determine the `.yaml` files that are generated. Within OpenClash, you can set each rule-provider yaml to a different server group. You may want to have a Netflix category with just ["netflix", "hulu"] as the value and set that to your USA server group, and a YouTube category with ["vimeo", "youtube"] as the value and set that to your HongKong server group. This is useful for load balancing as well as targeting specific region-locked content.|{"AdBlock": ["category-ads"],"Domestic": ["geolocation-cn"],"Microsoft": ["microsoft"],"select": ["geolocation-!cn", "github"]}|


## Recommended categories
Here is an example of my categories. To make the auto-update servers function properly with my Proxy Provider, a `select` Proxy Group is required, and this is probably different for you.

    categories = {
    	"AdBlock": ["categories-ads"],
    	"Amazon": ["amazon"],
    	"Apple": ["apple"],
    	"BBC": ["category-media"],
    	"Domestic": ["geolocation-cn"],
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
    	"Youtube": ["vimeo", "youtube"]
    }
#
### My OpenClash workflow (in case it helps anyone)
I set all US servers to be in a Proxy Group (Step 3) called USA, and all HongKong servers to be in a Proxy Group called UK, and so-on for other countries. I then have groups for various categories as seen in the **Recommended categories** above. This way, I can occasionally test the speeds of servers in America, and change to the fastest server from the USA group. Then, any other groups like Netflix or Spotify that I have pointing to the USA group will also go through the newly-selected server. I can also set something like BBC to UK servers for better iPlayer functionality, Netflix to USA for required functionality, YouTube to HK for speed, etc.

## To-do
* Add a `DOMAIN-KEYWORD,speedtest` option. Leaving this on all the time would likely catch domains unrelated to ookla-speedtest, but it's vital to ensuring speed test servers are routed through the specified proxies. *See [pull #157]([https://github.com/v2fly/domain-list-community/pull/157](https://github.com/v2fly/domain-list-community/pull/157)) in the domain-list-community repo.*
* Make script into a service to periodically pull updates from the `domain-list-community` repo to stay current.
* Create a Luci-App for configuration and usage from the Admin panel in OpenWRT. I would love for this functionality to be taken by the team working on OpenClash and integrated into their admin panel.
