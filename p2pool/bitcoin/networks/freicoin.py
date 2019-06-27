import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '2cfe7e6d'.decode('hex')
P2P_PORT = 8639
ADDRESS_VERSION = 0
RPC_PORT = 8638
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '000000005b1e3d23ecfd2dd4a6e1a35238aa0392c0a8528c40df52376d7efe2c')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = 9536743164
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'FRC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Freicoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Freicoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.freicoin'), 'freicoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://blockchain.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://blockchain.info/address/'
TX_EXPLORER_URL_PREFIX = 'https://blockchain.info/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
