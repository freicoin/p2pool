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
BOOTSTRAP_ADDRS = 'pool.freico.in asia-east1.gcp.pool.tradecraft.io asia-south1.gcp.pool.tradecraft.io australia-southeast1.gcp.pool.tradecraft.io europe-north1.gcp.pool.tradecraft.io northamerica-northeast1.gcp.pool.tradecraft.io southamerica-east1.gcp.pool.tradecraft.io us-west-2.aws.pool.tradecraft.io eu-west-1.aws.pool.tradecraft.io ap-northeast-1.aws.pool.traecraft.io'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-tfrc'
VERSION_CHECK = lambda v: None if 12010000 <= v else 'Freicoin version too old. Upgrade to v12.1 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set()
MINIMUM_PROTOCOL_VERSION = 3200
NEW_MINIMUM_PROTOCOL_VERSION = 3301
BLOCK_MAX_SIZE = 1000000
BLOCK_MAX_WEIGHT = 4000000
