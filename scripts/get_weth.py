from scripts.helpful_scripts import get_account
from brownie import interface, config, network, accounts

def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    # ABI 
    # Address
    account = get_account()
    print(f'ETH balance: {account.balance()}')
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    print(f'WETH balance: {interface.IWeth(weth).balanceOf(account)}')
    tx = weth.deposit({"from": account, "value": 0.01 * 10 ** 18})
    tx.wait(1)
    print("Received wETH")
    print(f'ETH balance: {account.balance()}')
    print(f'WETH balance: {interface.IWeth(weth).balanceOf(account)}')
    return tx

  