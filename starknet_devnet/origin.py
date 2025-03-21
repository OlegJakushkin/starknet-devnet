"""
Contains classes that provide the abstraction of L2 blockchain.
"""

from starknet_devnet.util import StarknetDevnetException, TxStatus


class Origin:
    """
    Abstraction of an L2 blockchain.
    """

    def get_transaction_status(self, transaction_hash: str):
        """Returns the status of the transaction."""
        raise NotImplementedError

    def get_transaction(self, transaction_hash: str):
        """Returns the transaction object."""
        raise NotImplementedError

    def get_block_by_hash(self, block_hash: str):
        """Returns the block identified with either its hash."""
        raise NotImplementedError

    def get_block_by_number(self, block_number: int):
        """Returns the block identified with either its number or the latest block if no number provided."""
        raise NotImplementedError

    def get_code(self, contract_address: int) -> dict:
        """Returns the code of the contract."""
        raise NotImplementedError

    def get_storage_at(self, contract_address: int, key: int) -> str:
        """Returns the storage identified with `key` at `contract_address`."""
        raise NotImplementedError

    def get_number_of_blocks(self):
        """Returns the number of blocks stored so far"""
        raise NotImplementedError


class NullOrigin(Origin):
    """
    A default class to comply with the Origin interface.
    """

    def get_transaction_status(self, transaction_hash: str):
        return {
            "tx_status": TxStatus.NOT_RECEIVED.name
        }

    def get_transaction(self, transaction_hash: str):
        return {
            "status": TxStatus.NOT_RECEIVED.name,
            "transaction_hash": transaction_hash
        }

    def get_block_by_hash(self, block_hash: str):
        message=f"Block hash not found; got: {block_hash}."
        raise StarknetDevnetException(message=message)

    def get_block_by_number(self, block_number: int):
        message = "Requested the latest block, but there are no blocks so far."
        raise StarknetDevnetException(message=message)

    def get_code(self, contract_address: int):
        return {
            "abi": {},
            "bytecode": []
        }

    def get_storage_at(self, contract_address: int, key: int) -> str:
        return hex(0)

    def get_number_of_blocks(self):
        return 0


class ForkedOrigin(Origin):
    """
    Abstracts an origin that the devnet was forked from.
    """

    def __init__(self, url):
        self.url = url
        self.number_of_blocks = ...

    def get_transaction_status(self, transaction_hash: str):
        raise NotImplementedError

    def get_transaction(self, transaction_hash: str):
        raise NotImplementedError

    def get_block_by_hash(self, block_hash: str):
        raise NotImplementedError

    def get_block_by_number(self, block_number: int):
        raise NotImplementedError

    def get_code(self, contract_address: int) -> dict:
        raise NotImplementedError

    def get_storage_at(self, contract_address: int, key: int) -> str:
        raise NotImplementedError

    def get_number_of_blocks(self):
        return self.number_of_blocks
