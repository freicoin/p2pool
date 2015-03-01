import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

try:
    from gmpy2 import mpq
except ImportError:
    from fractions import Fraction as mpq


P2P_PREFIX = '5ed67cf3'.decode('hex')
P2P_PORT = 18639
ADDRESS_VERSION = 111
RPC_PORT = 18638
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'freicoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: int(mpq((161280-height) * 15916928405, 161280) + mpq(9999999999999999, 1048576)) if height < 161280 else 9536743164
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'tFRC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Freicoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Freicoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.freicoin'), 'freicoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'http://blockexplorer.com/testnet/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
