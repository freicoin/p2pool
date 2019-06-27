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
BOOTSTRAP_ADDRS = 'pool.freico.in asia-east1.gcp.pool.tradecraft.io asia-south1.gcp.pool.tradecraft.io australia-southeast1.gcp.pool.tradecraft.io europe-north1.gcp.pool.tradecraft.io northamerica-northeast1.gcp.pool.tradecraft.io southamerica-east1.gcp.pool.tradecraft.io us-west-2.aws.pool.tradecraft.io eu-west-1.aws.pool.tradecraft.io ap-northeast-1.aws.pool.traecraft.io'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-frc'
VERSION_CHECK = lambda v: None if 12010000 <= v else 'Freicoin version too old. Upgrade to v12.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set()
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
