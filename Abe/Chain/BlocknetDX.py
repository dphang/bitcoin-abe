# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.
from .PpcPosChain import PpcPosChain


class BlocknetDX(PpcPosChain):
    """
    Blocknet, a Proof-of-Stake currency and decentralized exchange.
    """

    def __init__(chain, **kwargs):
        chain.name = 'BlocknetDX'
        chain.code3 = 'BLOCK'
        chain.address_version = "\x1A"
        chain.magic = "\xa1\xa0\xa2\xa3"
        PpcPosChain.__init__(chain, **kwargs)

    datadir_conf_file_name = "blocknetdx.conf"
    datadir_rpcport = 41414
