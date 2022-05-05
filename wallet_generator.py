import secrets
import eth_utils.exceptions
import argparse
from eth_keys import keys


def parse_args():
    parser = argparse.ArgumentParser(description='Ethereum Wallet Generator')

    parser.add_argument('-f', '--file',
                        required=True,
                        help='Specify filename to write wallets to.')
    parser.add_argument('-n', '--number',
                        type=int,
                        required=True,
                        help='Specify how many wallets to generate.')

    return parser.parse_args()


def generate_eth_wallet():
    valid = False
    while not valid:
        try:
            private_key = str(hex(secrets.randbits(256))[2:])
            private_key_bytes = bytes.fromhex(private_key)
            public_key_hex = keys.PrivateKey(private_key_bytes).public_key
            public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
            public_address = keys.PublicKey(public_key_bytes).to_address()
            checksum = keys.PublicKey(public_key_bytes).to_checksum_address()
            valid = True

            return public_address, checksum, private_key

        except ValueError:
            pass
        except eth_utils.exceptions.ValidationError:
            pass



def append_to_file(filename, public_key, private_key):
    file = open(filename, 'a')
    with file:
        file.write(f'\n{public_key},{private_key}')


def create_new_wallets_file(filename):
    file = open(filename, 'w')
    with file:
        file.write('Public_key,Private_key')


def main():
    args = parse_args()

    i = 0
    create_new_wallets_file(args.file)

    while i != args.number:
        eth_wallet_info = generate_eth_wallet()
        public_key = eth_wallet_info[0].lower()
        checksum = eth_wallet_info[1].lower()
        private_key = eth_wallet_info[2]

        if public_key == checksum:
            append_to_file(args.file, public_key, private_key)
            i += 1


if __name__ == '__main__':
    main()
