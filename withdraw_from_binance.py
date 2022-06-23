import logging
import math
import json

from matplotlib.style import available
from binance.spot import Spot as Client
from utils import get_env, precising_amount


# get api info
BINANCE_API_KEY, BINANCE_SECRET_KEY = get_env(get_binance_info=True)

# connect to exchange client
spot_client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)


def withdraw_from_binance(
    spot_client, coin_name, withdraw_amount, to_chain, to_address
):
    """withdraw token from binance exchange

    !! To make it work, you need to set up the api, fill the ip address and allow the withdrawal

    Args:
        spot_client (_type_): binance spot clinet
        coin_name (str): the name of the coin
        withdraw_amount (float): the amount to withdraw
        to_chain (_type_): the destination chain name
        to_address (_type_): the destination/withdraw address
    """

    to_chain = to_chain.upper()
    all_coin_info = spot_client.coin_info()
    coin_info = [coin for coin in all_coin_info if coin["coin"] == coin_name][0]
    to_chain_info = [
        network
        for network in coin_info["networkList"]
        if network["network"] == to_chain
    ][0]
    con_can_withdraw = (
        (to_chain_info["withdrawEnable"] == True)
        & (
            float(coin_info["free"])
            > withdraw_amount + float(to_chain_info["withdrawFee"])
        )
        & (withdraw_amount > float(to_chain_info["withdrawMin"]))
    )
    logging.info(f"withdrawEnable: {to_chain_info['withdrawEnable']}")
    logging.info(f"withdrawFee: {to_chain_info['withdrawFee']}")
    logging.info(f"withdrawMin: {to_chain_info['withdrawMin']}")
    logging.info(f"AvailableAmount: {coin_info['free']}")
    logging.info(f"withdrawIntegerMultiple: {to_chain_info['withdrawIntegerMultiple']}")
    logging.info(f"con_can_withdraw: {con_can_withdraw}")
    logging.info(float(to_chain_info["withdrawIntegerMultiple"]))
    logging.info(
        f"digit: {math.log10(float(to_chain_info['withdrawIntegerMultiple']))})"
    )

    withdraw_amount = float(
        precising_amount(
            withdraw_amount,
            int(-math.log10(float(to_chain_info["withdrawIntegerMultiple"]))),
        )
    )
    logging.info(f"withdraw_amount: {float(withdraw_amount)}")

    if con_can_withdraw:
        spot_client.withdraw(
            coin=coin_name, amount=withdraw_amount, network=to_chain, address=to_address
        )
        logging.info(f"Succeeded!")
    else:
        logging.info(f"Failed!")


def main():
    # read addresses
    with open("addresses.json", "r") as fp:
        list_addresses = json.load(fp)
    logging.info(f"Finished reading list of addresses.")

    withdraw_amount = 0.5
    coin_name = "ETH"
    to_chain = "BSC"
    # to_address = ""

    for address in list_addresses:
        to_address = address["address"]
        withdraw_from_binance(
            spot_client, coin_name, withdraw_amount, to_chain, to_address
        )


if __name__ == "__main__":
    loglevel = logging.INFO
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y/%m/%d %I:%M:%S",
        level=loglevel,
    )
    main()
