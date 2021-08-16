from libs.openexchange import OpenExchangeClient


APP_ID = "6d1ca72895a24ff389af101a53b288d0"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f"USD {usd_amount} is GBP {gbp_amount:.2f}.")