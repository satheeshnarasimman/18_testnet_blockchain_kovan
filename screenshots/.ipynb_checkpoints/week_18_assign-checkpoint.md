# week18_blockchain_basics_project
In this project, the steps for creating a testnet Blockchain for a fictious organization, ZBank is explained. These instructions have been performed on a Windows 10 64-bit laptop. Depending upon the operating system, the installation/ commands might be different.

## Tools/technologies used
- GoEthereum
- MyCrypto
- Gitbash
- Github
- VS Code
- Windows 10 64-Bit laptop

## Environment setup
Installation of MyCrypto and GoEthereum are required for the testnet.
- Install MyCrypto from the following link [MyCrypto](https://www.mycrypto.com/)
- Download [Go Ethereum](https://geth.ethereum.org/), one of the three Ethereum protocol implementations. Select the version that is appropriate for your operating system.
- Unzip the GoEthereum folder. This will be the directory that will be used for the testnet.

## Creating a proof of authority blockchain
- Navigate to the above folder and start gitbash from there.
- The following commands will create new nodes. Type them one by one and save the password on a text editor (VS Code).
    * ./geth --datadir node3 account new
    * ./geth --datadir node4 account new
    
- Run the `./puppeth` command and type a network name (zbank here).
- In the resulting prompts, select `configure new genesis` and `create new genesis from scratch` respectively.
- For the consensus engine choose `clique- proof-of-authority`.
- Save both the account addresses for the nodes on the text editor
- Should the precompile be prefunded with 1 wei? Choose `No`
- Specify the chain id. `1811` in this case. Save it.
- What would you like to do? `Manage existing genesis` and choose `export genesis configurations`.
- Now the genesis specifications json file will be created.
- Initialize the json files for both the nodes using `./geth --datadir node3 init zbank.json`. For node 4, simply substitute 4 inplace of 3.

- Thereafter, use the following command to set node3 to begin mining. The quote contains the public address of node3 without the leading '0x'
    * ./geth --datadir node3 --unlock "F7f8Dba8722BA611b61e1838e5a362B6f121B909" --mine --rpc --allow-insecure-unlock.
- Copy the enode address and save it. On a separate gitbash window, use the copied enode address inside the quotes after --bootnodes in the following command. Paste the public address of node4 after --unlock in the command.
    * ./geth --datadir node4 --unlock "e840Fecd8B4dF68B51F82769D6108CFa7902150c" --mine --port 30304 --bootnodes "enode://3d9607dc85c0a3cf43358b2887e2a3a506592561d8a31172eed345066f1bccc84779fbe153dae07ddfd88bf68c7ff3fd4dcc838792ab5c5e8210c2b957a2ed24@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock
    
- Now our nodes are mining blocks on the blockchain testnet. With the nodes running, test the blockchain on MyCrypto.

## Testing on MyCrypto
- Open the MyCrypto app, then click `Change Network` at the bottom left.
- Click "Add Custom Node", then add the custom network information that was created in the genesis.
- Choose `Custom` in the "Network" column to reveal `Chain ID` option.
- Type `ETH` in the Currency box.
- In the Chain ID box, type the chain id you generated during genesis creation.
- In the URL box type: `http://127.0.0.1:8545`.  This points to the default RPC port on your local machine.
- Finally, click `Save & Use Custom Node`.
- Select the `View & Send` from the left menu, then click `Keystore file`.
- On the next screen, click `Select Wallet File`, then navigate to the keystore directory inside Node3. 
- Upload the keystore file, provide your password when prompted and then click `Unlock`.
- This will open your account wallet inside MyCrypto.
- In the `To Address` box, type the account address from Node4, then choose an ETH amount to transfer.
- Select `Send Transaction`, and the "Send" button in the pop-up window.
- Hit `Check TX Status` and when the green message pops up, logout of the network.

The testnet blockchain for ZBank has now been configured

## Testnet specifications
- Blocktime: 15 seconds
- ChainID: 1811
- Network ID: 127.0.0.1:8545
- Node3 password: 1991
- Node4 password: 1992
- Test amount sent: 316,906,558 ETH

## Issues faced
- The amount in Node3 has changed, but the transaction status still shows 'Pending'.

## Contributors
- Satheesh Narasimman

## People who helped
- Khaled Karman, Bootcamp tutor

## References
- https://ucb.bootcampcontent.com/UCB-Coding-Bootcamp/ucb-sfc-fin-pt-08-2020-u-c/blob/master/02-Homework/18-Blockchain/Instructions/Resources/POA-Blockchain-guide.md