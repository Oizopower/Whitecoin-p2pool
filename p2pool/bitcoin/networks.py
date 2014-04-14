import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

@defer.inlineCallbacks
def get_subsidy(bitcoind, target):
    res = yield bitcoind.rpc_getblock(target)

    defer.returnValue(res)

nets = dict(
    whitecoin=math.Object(
        P2P_PREFIX='fef5abaa'.decode('hex'),
        P2P_PORT=15714,
        ADDRESS_VERSION=73,
        RPC_PORT=15715,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Whitecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda bitcoind, target: 30000*100000000,
        BLOCK_PERIOD=90, # s
        SYMBOL='WC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Whitecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Whitecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Whitecoin'), 'Whitecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://testnet/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.01e8,
    ),
    whitecoin_testnet=math.Object(
        P2P_PREFIX='fef5abaa'.decode('hex'),
        P2P_PORT=15714,
        ADDRESS_VERSION=73,
        RPC_PORT=15715,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Whitecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda bitcoind, target: 10000*100000000,
        BLOCK_PERIOD=90, # s
        SYMBOL='WC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'whiteCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/whiteCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.whitecoin'), 'whitecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://testnet/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.01e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
