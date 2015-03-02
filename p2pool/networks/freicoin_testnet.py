from p2pool.bitcoin import networks

PARENT = networks.nets['freicoin_testnet']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 60*60//10 # shares
REAL_CHAIN_LENGTH = 60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'a52504ffe3420a43'.decode('hex')
PREFIX = 'bd385ef24f818389'.decode('hex')
P2P_PORT = 19639
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 19638
BOOTSTRAP_ADDRS = 'pool.freico.in abacus.freico.in pool.sicanet.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-tfrc'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
