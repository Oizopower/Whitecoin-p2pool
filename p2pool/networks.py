from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    whitecoin=math.Object(
        PARENT=networks.nets['whitecoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=10, # blocks
        IDENTIFIER='10e037d5b8c69236'.decode('hex'),
        PREFIX='b07208c1a53ef659'.decode('hex'),
        P2P_PORT=8776,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8343,
        BOOTSTRAP_ADDRS='coins.inceptioncraft.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-wc',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
    whitecoin_testnet=math.Object(
        PARENT=networks.nets['whitecoin_testnet'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=10, # blocks
        IDENTIFIER='e037d5b8c7923110'.decode('hex'),
        PREFIX='7208c1a54ef619b0'.decode('hex'),
        P2P_PORT=18777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS='coins.inceptioncraft.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60011,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
