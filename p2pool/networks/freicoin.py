from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['freicoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '5b1e3d23ecfd2dd4'.decode('hex')
PREFIX = 'a6e1a35238aa0392'.decode('hex')
P2P_PORT = 9639
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 9638
BOOTSTRAP_ADDRS = 'pool.freico.in abacus.freico.in pool.sicanet.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-frc'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
VERSION_WARNING = lambda v: 'Upgrade Freicoin to >=0.8.5!' if v < 80500 else None
