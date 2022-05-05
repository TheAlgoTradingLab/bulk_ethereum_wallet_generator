# Ethereum wallet generator
This is a simple script to quickly generate ETH wallet addresses to a .csv file.

It validates the address through eth-keys lib and additionally checks if the checksum matches public address before saving them to a file.

## Python dependencies
- eth-keys https://pypi.org/project/eth-keys/
- pysha3 https://pypi.python.org/pypi/pysha3
- argparse https://pypi.org/project/argparse/

To quickly install python dependencies run
```bash
pip install -r requirements.txt
```

## Usage
Simply run the following command
```bash
python3 wallet_generator.py -file wallets.csv -number 500
```

## Output
```bash
Public_key,Private_key
0xd51a3a8cd70f4533e1bd29c68f1f184612e844a1,b17436bf4f73ae3a9d3c1158ba6b9207d238a09f09e66983c8cef27091a00568
0xf440e3ccc39d97fc2ced63bd99604a93a6f3ee4a,64d2380e5c3b205188e82d6cd21a7ad0ec93fd98b37d5c14fc18f5edf1faeb5a
0xba92ac843213edc6c83de89435a48adda913b1f3,611842b59cedaff005de0c1bdb8f668ec8caef896721c6e16d631ad4e5c8fc69
0x084533cc8992d5913975df149e4a3a75418ffbea,50b1206dc8f3676fe7e25b608ab45f396ee21802e9e4f7253d3daf4dc7a5be72
0x38de14e6438f45fc10ff57cb73c2f523f532d718,c0c6f110459f9038445ec005a7ad247c4e8a252d6cecf268a01e6653ec9c839c
```