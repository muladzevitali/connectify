# Facebook Graph API connection

## Supported actions

Currently, we support the following functionalities from Graph API inside FacebookConnection class

1. [get_login_url](facebook_connection.py) - Generate login URL with given scope of permissions to get access code and
   then access token from Graph API
2. [get_ads_related_auth_url](facebook_connection.py) - Generate login URL for ads related permissions
3. [get_access_token](facebook_connection.py) - Get access token from the access code fetched from the steps 1 or 2
4. [get_ad_accounts[^1]](facebook_connection.py) - Get ad accounts existing under the access token initialize the class
   with.
5. [get_ad_account_campaigns[^1]](facebook_connection.py) - Get campaigns under given ad account
6. [get_ad_campaign_ad_sets[^1]](facebook_connection.py) - Get ad sets under given campaign
7. [get_ad_set_ads[^1]](facebook_connection.py) - Get ads under given ad set

[^1]:  In this case you only need to initialize class with **access_token** argument

## Requirements
```shell
facebook-sdk>=3.1.0
```