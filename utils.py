import os
from dotenv import load_dotenv


def get_env(get_binance_info=False):
    """get dot env variables from .env file

    Returns:
        string: ZB_API_KEY
    """

    load_dotenv()  # take environment variables from .env.

    CONTRACT_ADDRESS = os.environ.get("CONTRACT_ADDRESS")
    RINKEBY_PUBLIC_INFURA_ENDPOINT = os.environ.get("RINKEBY_PUBLIC_INFURA_ENDPOINT")
    MAINNET_PUBLIC_INFURA_ENDPOINT = os.environ.get("MAINNET_PUBLIC_INFURA_ENDPOINT")
    CHAIN_ID = os.environ.get("CHAIN_ID")
    BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
    BINANCE_SECRET_KEY = os.environ.get("BINANCE_SECRET_KEY")

    if get_binance_info:
        return (BINANCE_API_KEY, BINANCE_SECRET_KEY)

    return (
        CONTRACT_ADDRESS,
        RINKEBY_PUBLIC_INFURA_ENDPOINT,
        MAINNET_PUBLIC_INFURA_ENDPOINT,
        CHAIN_ID,
    )


def precising_amount(amount, digit):
    """
    Convert decimal point accuracy
    if using round, np.round, the small decimals would still remain
    :param amount:
    :param digit:
    :return:
    """
    w = "{" + f":.{digit}f" + "}"
    return w.format(amount)
