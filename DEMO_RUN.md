# 🎮 How to Run the Demo

## Quick Start (Hash Version - Simple)

### 1. Install Dependencies

```bash
# Root (kontrakty)
npm install

# Website
cd website && npm install && cd ..

# Bot
cd bot && npm install && cd ..
```

### 2. Uruchom Blockchain (Terminal 1)

```bash
npx hardhat node
```

**Keep this terminal open!** You'll see 20 test accounts.

### 3. Deploy Contract (Terminal 2)

```bash
npx hardhat deploy --network localhost
```

**IMPORTANT:** Copy the contract address from the output! It will look like:
```
OnchainRiddle contract: 0x5FbDB2315678afecb367f032d93F642f64180aa3
```

### 4. Configure Bot (Terminal 3)

```bash
cd bot
cp .env.example .env
```

Edit `bot/.env`:
```bash
CONTRACT_ADDRESS=0x5FbDB2315678afecb367f032d93F642f64180aa3  # Your address!
```

Run the bot:
```bash
npm run dev
```

The bot will automatically set the first riddle after 5 seconds! 🤖

### 5. Run Website (Terminal 4)

```bash
cd website
```

Edit `website/src/lib/contract.ts`, line 1:
```typescript
export const ONCHAIN_RIDDLE_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"; // Your address!
```

Run it:
```bash
npm run dev
```

### 6. Play! 🎉

1. Open http://localhost:3000
2. Click "Connect Wallet"
3. In MetaMask:
   - Add Hardhat Local network:
     - Network Name: `Hardhat Local`
     - RPC URL: `http://127.0.0.1:8545`
     - Chain ID: `31337`
     - Currency: `ETH`
   - Import a test account (NOT the first one - that's the bot!)
     - Get private key from Terminal 1
4. Read the riddle
5. Type your answer
6. Win! 🏆

### Test Answers

The bot has 15 riddles. First few:
- "What has keys but no locks?" → `keyboard`
- "I speak without a mouth and hear without ears. What am I?" → `echo`
- "What has hands but cannot clap?" → `clock`

**All answers are lowercase!**

## Testing with Hardhat Tasks

You can also test from the terminal:

```bash
# View current riddle
npx hardhat task:get-riddle --network localhost

# Submit answer
npx hardhat task:submit-answer --answer "keyboard" --network localhost

# Set new riddle (bot only)
npx hardhat task:set-riddle --riddle "Your riddle?" --answer "answer" --network localhost
```

## Troubleshooting

### "Contract address not found"
- Check if you copied the address from deploy
- Check if Hardhat node is still running

### "Transaction failed"
- Make sure you're using a DIFFERENT account than the first one (that's the bot)
- Reset MetaMask: Settings → Advanced → Clear activity data

### Bot not setting riddles
- Check if address in `bot/.env` is correct
- Check if private key is from the FIRST account (bot)

### Website not connecting
- Check if address in `website/src/lib/contract.ts` is correct
- Check if port 3000 is available

## FHE Version (Advanced)

FHE version requires:
1. Newer version of `@fhevm/solidity` with Gateway
2. fhEVM network (not Hardhat)
3. FHE encryption in website and bot

See `FHE_UPGRADE.md` and `contracts/GATEWAY_EXPLANATION.md` for details.

## Quick Commands Cheat Sheet

```bash
# Start wszystkiego (4 terminale):
Terminal 1: npx hardhat node
Terminal 2: npx hardhat deploy --network localhost
Terminal 3: cd bot && npm run dev
Terminal 4: cd website && npm run dev

# Contract tests:
npm test

# Formatting:
npm run prettier:write

# Linting:
npm run lint
```

## Architecture Flow

```
┌─────────────┐
│   Website   │ ← Player connects wallet
│ localhost:  │   and submits answers
│    3000     │
└──────┬──────┘
       │
       ↓
┌─────────────────┐      ┌──────────────┐
│  Smart Contract │ ←────│     Bot      │
│  OnchainRiddle  │      │  Listens for │
│   on Hardhat    │      │   Winner     │
└─────────────────┘      │   events     │
                         └──────────────┘
```

When player wins → Bot sees event → Posts new riddle → Cycle repeats! 🔄

## What's Next?

1. **Deploy to Sepolia:**
   ```bash
   npx hardhat deploy --network sepolia
   ```

2. **Add your own riddles:**
   Edit `bot/src/riddles.ts`

3. **Customize UI:**
   Change colors in `website/src/`

Happy riddling! 🧩
