# Jungo Echo Subnet 

The repository demonstrate a simple subnet in jungoai and can be use as a template to develop a new subnet and also learn
how to run a node (worker or monitor) in a jungoai subnet.

Currently echo-subnet is running on jungoai devnet and available for running node and testing.

In the following tutorial we are going to run a worker node and a monitor node in the echo-subnet on jungoai devnet.

*Table of contents:*
- Installation
- Setup Wallets
    - Create coldkeys
    - Create hotkeys
- Get token
- Run a Worker
- Run a Monitor

# Installation

[Install rye](https://rye.astral.sh/guide/installation/):

```bash
curl -sSf https://rye.astral.sh/get | bash
```

Then install Echo Subnet via `rye`:

``` bash
rye install echo-subnet --git https://github.com/jungoai/jungo-echo-subnet.git
```

# Set up Wallets

[Install jungo-cli](https://github.com/jungoai/jungo-cli?tab=readme-ov-file#installation)

```bash
rye install jungo-cli --git https://github.com/jungoai/jungo-cli.git
```

## Create Coldkeys (wallet name)


```bash
jucli wallet new_coldkey
```

Enter the path of your wallet. Default is `~/.jungoai/wallets/`, press enter or write another path as you want.
```
Enter the path to the wallets directory (~/.jungoai/wallets/):
```

Enter your desire name for your coldkey (wallet name). In this example we use `alan`
```
Enter the wallet name (default): alan
```

Write number of words for secret phrase.
```
Choose the number of words [12/15/18/21/24]:
```

Write a password for your wallet.
```
Enter your password:
```

Save your mnemonic in a safe place, it will used to recover the coldkey.
```
The mnemonic to the new coldkey is: ...
```

Check your wallet.
```bash
jucli wallet list
```

## Create Hotkeys

A hotkey is another address that placed under a coldkey.
The coldkey is used to hold and transfer tokens. A hotkey (alongside coldkey) is used to
register node (worker or monitor) and get staked to get reward in jungoai ecosystem.
The purpose of hotkey is to provide more security, coldkey for causal use like transfer tokens, and hotkey to be used in 
jungoai ecosystem.

In this tutorial we need to hotkey, one for worker, one for monitor.

```bash
jucli wallet new_hotkey
```

And filled the prompt. For example:
```
Enter the wallet name (default): alan
Enter the name of the new hotkey (default): echoWorker
Enter the wallet path (Hint: You can set this with `jucli config set --wallet-path`) (~/.jungoai/wallets/):
Choose the number of words [12/15/18/21/24]: 12
```

Check your wallet.
```bash
jucli wallet list
```

Now create a new hotkey named `echoMonitor` for `alan` coldkey just like before.

# Get Token

TODO

# Run a Worker

Register a node in the echo-subnet (it's netuid 1001)

```bash
jucli subnet register --name alan --hotkey echoWorker --netuid 1001 --chain devnet
```

Turn the node to an echo worker:

```bash
echo-worker                     \
    --ip            HOST_IP     \
    --port          PORT        \
    --netuid        1001        \
    --wallet.name   alan        \
    --wallet.hotkey echoWorker  \
    --chain         wss://devnet-rpc.jungoai.xyz \
    --logging.debug
```

- `HOST_IP` should be your static ip of your server
- `PORT` would be your desire port
- `--logging.debug` is optional

To get reward you need an amount of stake to your hotkey `echoWorker`:

```bash
jucli stake add --amount 100 --name alan --hotkey echoWorker --chain devnet
```

Check your node:

```bash
jucli wallet overview --name alan --chain devnet
```

After amount of time, e.g 1 hour later, you can check it again to ensure the emission you'd got.

# Run a Monitor

<!-- To run a monitor you need to register a node in root subnet (subnet 0) and a node with the same hotkey in  -->
<!-- echo-subnet (subnet 1001) -->

<!-- Register a node in root subnet : -->

Register a new node in the echo-subnet (it's netuid 1001)

```bash
jucli subnet register --name alan --hotkey echoWorker --netuid 1001 --chain devnet
```

Turn the node to an echo monitor:

```bash
echo-monitor \
    --wallet.name   alan        \
    --wallet.hotkey echoMonitor \
    --netuid        1001        \
    --chain         wss://devnet-rpc.jungoai.xyz \
    --logging.debug 
```

Add stake to your hotkey `echoWorker`:

```bash
jucli stake add --amount 100 --name alan --hotkey echoWorker --chain devnet
```

Check your node after a while:

```bash
jucli wallet overview --name alan --chain devnet
```
