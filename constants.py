from enum import Enum
import os

DATA_DIRECTORY = 'tmp/data'
JSON_DATA_DIRECTORY = os.path.join(DATA_DIRECTORY,"json_data")
RAW_REQUESTS_DIRECTORY = os.path.join(DATA_DIRECTORY,"raw_requests")

os.makedirs(DATA_DIRECTORY,exist_ok=True)
os.makedirs(JSON_DATA_DIRECTORY,exist_ok=True)
os.makedirs(RAW_REQUESTS_DIRECTORY,exist_ok=True)

class CrawlerBaseURLs(Enum):
    BASE_URL = "https://www.amazon.com/s"

class CrawlerConstants(Enum):
    COOKIES = {
    'aws-ubid-main': '157-3587214-4280557',
    'session-id': '146-7955194-3549945',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'USD',
    'ubid-main': '131-2000831-2243815',
    'lc-main': 'en_US',
    'aws-userInfo': '%7B%22arn%22%3A%22arn%3Aaws%3Asts%3A%3A357166116729%3Aassumed-role%2FAWSReservedSSO_PowerUserAccess_581ba15f0484c33d%2Fshujaat_ali%22%2C%22alias%22%3A%22357166116729%22%2C%22username%22%3A%22assumed-role%252FAWSReservedSSO_PowerUserAccess_581ba15f0484c33d%252Fshujaat_ali%22%2C%22keybase%22%3A%22pD%2FIDb534OsljMEm5n27XPNV6EwSKaRqJs%2Bc1Cg2gKg%5Cu003d%22%2C%22issuer%22%3A%22https%3A%2F%2Fcodeaza.awsapps.com%2Fstart%2F%23%2Fconsole%3Faccount_id%5Cu003d357166116729%5Cu0026role_name%5Cu003dPowerUserAccess%5Cu0026destination%5Cu003dhttps%253A%252F%252Fconsole.aws.amazon.com%22%2C%22signinType%22%3A%22PUBLIC%22%7D',
    'aws-userInfo-signed': 'eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjcwZjQzOWQ3LTBlNmYtNDgwYy1hYTc2LTEzZGMzZGY1ZDM5MyJ9.eyJzdWIiOiIzNTcxNjYxMTY3MjkiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cHM6XC9cL2NvZGVhemEuYXdzYXBwcy5jb21cL3N0YXJ0XC8jXC9jb25zb2xlP2FjY291bnRfaWQ9MzU3MTY2MTE2NzI5JnJvbGVfbmFtZT1Qb3dlclVzZXJBY2Nlc3MmZGVzdGluYXRpb249aHR0cHMlM0ElMkYlMkZjb25zb2xlLmF3cy5hbWF6b24uY29tIiwia2V5YmFzZSI6InBEXC9JRGI1MzRPc2xqTUVtNW4yN1hQTlY2RXdTS2FScUpzK2MxQ2cyZ0tnPSIsImFybiI6ImFybjphd3M6c3RzOjozNTcxNjYxMTY3Mjk6YXNzdW1lZC1yb2xlXC9BV1NSZXNlcnZlZFNTT19Qb3dlclVzZXJBY2Nlc3NfNTgxYmExNWYwNDg0YzMzZFwvc2h1amFhdF9hbGkiLCJ1c2VybmFtZSI6ImFzc3VtZWQtcm9sZSUyRkFXU1Jlc2VydmVkU1NPX1Bvd2VyVXNlckFjY2Vzc181ODFiYTE1ZjA0ODRjMzNkJTJGc2h1amFhdF9hbGkifQ.z52TP1oezQka4ZSeKLZaX_vc2N0MELBxph7Zm7mzxynA_Qx9cW9-Dj7yjBOLwTktzHGu4ssM8ochIqNbhEo97cgLss7RHrKt31Fp06iXMFNd078gdW33HgCOgJEkGpUM',
    'noflush_awsccs_sid': '3ddcbe1a5e36177821fd3d4f956339af408b1f8c396f43d7a945af57fabea7fb',
    'sp-cdn': '"L5Z9:PK"',
    'skin': 'noskin',
    'session-token': 'MU6X5DRc3kqL/is5Y2YZfAweGamXqEYKxiS+pifpqDMH1uMcclmcn9IkltAQNG8Wwt5RvygZcefb2Zo0EWPTBjJy5n/cWtWVTGVpxBEWaOMWSCMc1Qqf9h8xXo3x5cAW+0GyStHbXEMTVkc714cnKzxbbmZLB6Op/SVvn/ZZBHlvNsXMyH7SEfRT+MzhTwmmxk4aor8iEnwabWZRsyPfEsPL5vOakfdKUy7AV8VcIHfBQzXJAee6D7LAgtrkK7zreVmIuI1EKMld3k6op5eWLM6cc0aX9bIfJN4JmUCgXe2JSG1ih01LGwRA8QAqyjEXhCqVeWwHeiliaOhKq+EFLEhZNmyxZzUO',
    'csm-hit': 'tb:s-QTN0T6S0PZGCF658ZQ1B|1726825267300&t:1726825268305&adb:adblk_no',
    }

    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'aws-ubid-main=157-3587214-4280557; session-id=146-7955194-3549945; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=131-2000831-2243815; lc-main=en_US; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Asts%3A%3A357166116729%3Aassumed-role%2FAWSReservedSSO_PowerUserAccess_581ba15f0484c33d%2Fshujaat_ali%22%2C%22alias%22%3A%22357166116729%22%2C%22username%22%3A%22assumed-role%252FAWSReservedSSO_PowerUserAccess_581ba15f0484c33d%252Fshujaat_ali%22%2C%22keybase%22%3A%22pD%2FIDb534OsljMEm5n27XPNV6EwSKaRqJs%2Bc1Cg2gKg%5Cu003d%22%2C%22issuer%22%3A%22https%3A%2F%2Fcodeaza.awsapps.com%2Fstart%2F%23%2Fconsole%3Faccount_id%5Cu003d357166116729%5Cu0026role_name%5Cu003dPowerUserAccess%5Cu0026destination%5Cu003dhttps%253A%252F%252Fconsole.aws.amazon.com%22%2C%22signinType%22%3A%22PUBLIC%22%7D; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjcwZjQzOWQ3LTBlNmYtNDgwYy1hYTc2LTEzZGMzZGY1ZDM5MyJ9.eyJzdWIiOiIzNTcxNjYxMTY3MjkiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cHM6XC9cL2NvZGVhemEuYXdzYXBwcy5jb21cL3N0YXJ0XC8jXC9jb25zb2xlP2FjY291bnRfaWQ9MzU3MTY2MTE2NzI5JnJvbGVfbmFtZT1Qb3dlclVzZXJBY2Nlc3MmZGVzdGluYXRpb249aHR0cHMlM0ElMkYlMkZjb25zb2xlLmF3cy5hbWF6b24uY29tIiwia2V5YmFzZSI6InBEXC9JRGI1MzRPc2xqTUVtNW4yN1hQTlY2RXdTS2FScUpzK2MxQ2cyZ0tnPSIsImFybiI6ImFybjphd3M6c3RzOjozNTcxNjYxMTY3Mjk6YXNzdW1lZC1yb2xlXC9BV1NSZXNlcnZlZFNTT19Qb3dlclVzZXJBY2Nlc3NfNTgxYmExNWYwNDg0YzMzZFwvc2h1amFhdF9hbGkiLCJ1c2VybmFtZSI6ImFzc3VtZWQtcm9sZSUyRkFXU1Jlc2VydmVkU1NPX1Bvd2VyVXNlckFjY2Vzc181ODFiYTE1ZjA0ODRjMzNkJTJGc2h1amFhdF9hbGkifQ.z52TP1oezQka4ZSeKLZaX_vc2N0MELBxph7Zm7mzxynA_Qx9cW9-Dj7yjBOLwTktzHGu4ssM8ochIqNbhEo97cgLss7RHrKt31Fp06iXMFNd078gdW33HgCOgJEkGpUM; noflush_awsccs_sid=3ddcbe1a5e36177821fd3d4f956339af408b1f8c396f43d7a945af57fabea7fb; sp-cdn="L5Z9:PK"; skin=noskin; session-token=MU6X5DRc3kqL/is5Y2YZfAweGamXqEYKxiS+pifpqDMH1uMcclmcn9IkltAQNG8Wwt5RvygZcefb2Zo0EWPTBjJy5n/cWtWVTGVpxBEWaOMWSCMc1Qqf9h8xXo3x5cAW+0GyStHbXEMTVkc714cnKzxbbmZLB6Op/SVvn/ZZBHlvNsXMyH7SEfRT+MzhTwmmxk4aor8iEnwabWZRsyPfEsPL5vOakfdKUy7AV8VcIHfBQzXJAee6D7LAgtrkK7zreVmIuI1EKMld3k6op5eWLM6cc0aX9bIfJN4JmUCgXe2JSG1ih01LGwRA8QAqyjEXhCqVeWwHeiliaOhKq+EFLEhZNmyxZzUO; csm-hit=tb:s-QTN0T6S0PZGCF658ZQ1B|1726825267300&t:1726825268305&adb:adblk_no',
        'device-memory': '8',
        'downlink': '9.15',
        'dpr': '1',
        'ect': '4g',
        'priority': 'u=0, i',
        'referer': 'https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=159651196451&hvpone=&hvptwo=&hvadid=675114638556&hvpos=&hvnetw=g&hvrand=3628746742601099132&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9195804&hvtargid=kwd-10573980&hydadcr=2246_13649807',
        'rtt': '200',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-viewport-width': '722',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'viewport-width': '722',
    }

    PARAMS = {
        'k': 'gaming headsets',
        '_encoding': 'UTF8',
        'content-id': 'amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a',
        'pd_rd_r': '5a21527a-881a-4938-82a7-725b05edd3bc',
        'pd_rd_w': 'iuFMp',
        'pd_rd_wg': 'slBGp',
        'pf_rd_p': '12129333-2117-4490-9c17-6d31baf0582a',
        'pf_rd_r': '8D6RJHXDVSFJJZG3F2MR',
        'ref': 'pd_hp_d_atf_unk',
    }

class SelectorsConstants(Enum):
    PRODUCT_URL_XPATHS = '//h2[contains(@class,"a-size-mini")]//a//@href'
    PRODUCT_TITLE_XPATH = '//h1[@id="title"]/span/text()'
    PRODUCT_PRICE_XPATH = '//div[contains(@class,"a-box")]//span[contains(@class,"a-price")]/span[contains(@class,"a-offscreen")]/text()'
    PRODUCT_COLOR_AND_EDITION_XPATH = '//span[@class="selection"]//text()'
    PRICE_Second_Xpath = '//div[contains(@class,"a-box")]//div[contains(@class,"a-column")]//span[contains(@class,"a-size-base")]/text()'
    NEXT_PAGE_XPATH = '//a[contains(@aria-label,"Go to next page")]/@href'
    XPATH_FOR_RATINGS = '//a[contains(@id,"acrCustomerReviewLink")]/span[contains(@id,"acrCustomerReviewText")]/text()'
    XPATH_FOR_FEATURES = '//tr[contains(@class,"a-spacing-small")]//span[contains(@class,"po-break-word")]/text()'
    
class AirTableConstants(Enum):
    TABLE_NAME = "Amazon products"