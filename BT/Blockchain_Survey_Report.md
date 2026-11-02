# Survey Report: Types of Blockchain and Their Real-Time Use Cases

**Course:** Laboratory Practice III (BE Computer Engineering)
**Group C – Blockchain Technology, Mini Project**

---

## Objective

To study blockchain technology, the different types of blockchain, and their applications, and to carry out a detailed survey of one real-world use case.

---

## 1. Introduction to Blockchain

A **blockchain** is a distributed, decentralized digital ledger that records transactions across many computers (nodes) so that no recorded entry can be changed afterwards without changing every later entry and getting agreement from the network.

In a traditional system, a central authority such as a bank keeps the ledger and everyone has to trust it. In a blockchain, every participating node keeps its own copy of the ledger, and new entries are added only when the nodes agree on them through a **consensus mechanism**. No middleman is needed.

The idea first appeared in practice with **Bitcoin**, launched in 2009 by the pseudonymous **Satoshi Nakamoto**. In 2015, **Ethereum** (proposed by Vitalik Buterin) extended the idea by letting programs called **smart contracts** run on the blockchain.

### 1.1 Structure of a Blockchain

The ledger is made of **blocks**. Each block contains:

- **Data**: a list of transactions
- **Timestamp**: when the block was created
- **Hash**: a unique fingerprint of the block's contents (e.g. SHA-256)
- **Previous hash**: the hash of the block before it

Because every block stores the previous block's hash, the blocks form a **chain**:

```
+-----------------+     +-----------------+     +-----------------+
|   Block 1       |     |   Block 2       |     |   Block 3       |
| (Genesis block) |     |                 |     |                 |
| Data: Tx...     |     | Data: Tx...     |     | Data: Tx...     |
| Prev: 0000      |<----| Prev: A1F3      |<----| Prev: 7C2B      |
| Hash: A1F3      |     | Hash: 7C2B      |     | Hash: E94D      |
+-----------------+     +-----------------+     +-----------------+
```

If someone changes the data in Block 2, its hash changes. Block 3 still holds the old hash, so the link breaks and the tampering is detected immediately. This is what makes a blockchain **immutable**.

### 1.2 How a Transaction Is Added

1. A user creates a transaction and **signs it with their private key**.
2. The transaction is broadcast to the peer-to-peer network.
3. Nodes **verify** the signature and check that the sender has enough balance.
4. Valid transactions are grouped into a new block.
5. The network agrees on the block using a **consensus mechanism**.
6. The block is added to the chain, and every node updates its copy.

### 1.3 Consensus Mechanisms

| Mechanism | How it works | Used by |
|---|---|---|
| **Proof of Work (PoW)** | Miners compete to solve a hard mathematical puzzle; the winner adds the block and earns a reward. Secure but uses a lot of electricity. | Bitcoin |
| **Proof of Stake (PoS)** | Validators lock up ("stake") coins and are chosen to propose blocks; dishonest validators lose their stake. Uses far less energy. | Ethereum (since 2022) |
| **Practical Byzantine Fault Tolerance (PBFT)** | Known, permissioned nodes vote on each block; works even if some nodes are faulty. Fast, but suited to smaller networks. | Hyperledger Fabric (variants) |
| **Proof of Authority (PoA)** | A small set of approved, identified validators create blocks. | Private and test networks |

### 1.4 Key Features of Blockchain

- **Decentralization**: no single owner or central authority.
- **Distributed ledger**: every node holds a copy of the data.
- **Immutability**: recorded data cannot be altered.
- **Transparency**: on public blockchains, anyone can view transactions.
- **Security**: cryptographic hashing and digital signatures protect the data.
- **Consensus**: nodes must agree before data is added.
- **Peer-to-peer transactions**: value moves directly between parties.
- **Traceability**: the full history of every asset can be followed.

---

## 2. Types of Blockchain

Blockchains are classified by **who can join the network** and **who can validate transactions**.

### 2.1 Public Blockchain

A **permissionless** network that anyone can join, read, send transactions to, and help validate. It is fully decentralized.

- **Examples:** Bitcoin, Ethereum, Litecoin
- **Advantages:** fully decentralized, highly transparent, resistant to censorship, secure because of the large number of nodes
- **Disadvantages:** slower and less scalable, high energy use (for PoW), transaction fees can rise when the network is busy, little privacy
- **Uses:** cryptocurrencies, public smart contracts, decentralized finance (DeFi), NFTs

### 2.2 Private Blockchain

A **permissioned** network controlled by a **single organization**. Only invited participants can join, and the organization decides who can read or write data.

- **Examples:** Hyperledger Fabric (deployed privately), R3 Corda (private deployments), Ripple's internal ledgers
- **Advantages:** fast, high throughput, private, low transaction cost, easier to meet regulations
- **Disadvantages:** partly centralized, so participants must trust the controlling organization; fewer nodes means it is easier to tamper with
- **Uses:** internal auditing, supply chain inside one company, asset management, internal record-keeping

### 2.3 Consortium (Federated) Blockchain

A **permissioned** network governed by a **group of organizations** rather than one. Validation is done by a set of pre-selected nodes, typically one or more per member organization.

- **Examples:** R3 Corda (banking consortium), Energy Web Chain, IBM Food Trust (built on Hyperledger Fabric)
- **Advantages:** more decentralized than a private chain, efficient and fast, privacy between members, shared cost
- **Disadvantages:** harder to set up because members must agree on governance; less transparent than a public chain
- **Uses:** inter-bank payments, trade finance, industry-wide supply chains, insurance

### 2.4 Hybrid Blockchain

A **combination of public and private** blockchains. Some data is kept private and permissioned, while selected data or proofs are made public for verification.

- **Examples:** Dragonchain, XinFin (XDC Network)
- **Advantages:** flexible control over what is public or private, good privacy with public verifiability, scalable
- **Disadvantages:** complex to design, less transparent than a fully public chain
- **Uses:** healthcare records, real estate, government services, regulated industries

### 2.5 Comparison of Blockchain Types

| Feature | Public | Private | Consortium | Hybrid |
|---|---|---|---|---|
| **Access** | Anyone | Invited only | Member organizations | Mixed |
| **Permission** | Permissionless | Permissioned | Permissioned | Both |
| **Controlled by** | No one (community) | One organization | Group of organizations | One organization + public network |
| **Decentralization** | Full | Low | Partial | Partial |
| **Speed** | Slow | Fast | Fast | Fast |
| **Transparency** | Full | Low | Among members | Selective |
| **Consensus** | PoW / PoS | PBFT / PoA / Raft | PBFT / PoA | Varies |
| **Example** | Bitcoin, Ethereum | Hyperledger Fabric | R3 Corda, IBM Food Trust | Dragonchain, XDC |

---

## 3. Real-Time Applications of Blockchain

| Sector | How blockchain is used | Example |
|---|---|---|
| **Cryptocurrency and payments** | Digital money that moves peer-to-peer without banks | Bitcoin, Ethereum |
| **Cross-border payments** | Fast, low-cost international transfers between banks | RippleNet, JPMorgan's Kinexys (formerly Onyx) |
| **Supply chain** | Tracks products from origin to customer; proves authenticity | IBM Food Trust (Walmart), De Beers Tracr (diamonds) |
| **Healthcare** | Secure, shareable patient records; tracking of medicines to stop counterfeits | MediLedger (drug supply chain) |
| **Voting** | Tamper-proof, verifiable digital votes | Pilots in several countries and organizations |
| **Land and property registry** | Records ownership so titles cannot be forged | Pilots in Georgia, Sweden and Indian states (e.g. Andhra Pradesh) |
| **Digital identity** | Users control their own verified identity | Self-sovereign identity projects |
| **Education** | Tamper-proof degree certificates that anyone can verify | MIT Blockcerts |
| **Insurance** | Smart contracts pay claims automatically when conditions are met | Flight-delay insurance pilots |
| **NFTs and digital ownership** | Unique tokens proving ownership of digital art, music or game items | Ethereum ERC-721 tokens |
| **Decentralized finance (DeFi)** | Lending, borrowing and trading without banks, using smart contracts | Uniswap, Aave |
| **Internet of Things (IoT)** | Secure data exchange between connected devices | Energy-trading and smart-grid pilots |

---

## 4. Detailed Survey of One Use Case: Food Supply Chain Traceability (IBM Food Trust and Walmart)

### 4.1 The Problem

Food passes through many hands before it reaches a customer: farmer → packer → processor → distributor → warehouse → retail store. Each party keeps its own records, often on paper or in separate systems that do not talk to each other.

When there is a food-safety outbreak (for example, E. coli in leafy greens), it can take **days or weeks** to find where the contaminated food came from. During that time, retailers often have to throw away large amounts of safe food as a precaution, and people may keep getting sick. Paper records can also be lost, incomplete, or falsified, which makes food fraud possible.

### 4.2 The Blockchain Solution

**IBM Food Trust** is a blockchain-based traceability network built on **Hyperledger Fabric**. It was piloted with **Walmart** starting in 2016 and launched commercially in **2018**. Other members have included Nestlé, Unilever, Dole, Tyson Foods, Kroger and Carrefour.

**Type of blockchain:** it is a **permissioned consortium blockchain**. Only verified supply-chain members can join, and each organization controls who can see its data. A public blockchain would expose business data and be too slow, while a single-company private chain would not be trusted by competitors. A consortium model gives shared trust with privacy.

### 4.3 How It Works

1. **At the farm**, the farmer records details of each batch: farm location, harvest date, and certifications.
2. **At each later step** (packing, shipping, storage), the handler scans the batch and adds a record: time, location, temperature, and so on.
3. Each record is added as a transaction to the shared ledger, which all authorized members can see.
4. Because the ledger is **immutable**, no party can later change or delete a record.
5. **At the store or by the customer**, scanning the product shows its full journey from farm to shelf.

```
Farm --> Packing house --> Distributor --> Warehouse --> Store --> Customer
  |           |                |              |           |
  +-----------+----------------+--------------+-----------+
                               |
                 Shared, immutable blockchain ledger
              (every step recorded with time, place, data)
```

### 4.4 Results

- **Traceability time:** in a test, Walmart traced a package of sliced mangoes back to its farm. With the old paper-based process it took **about 7 days** (6 days, 18 hours and 26 minutes). With the blockchain system it took **2.2 seconds**.
- **Pork in China:** an early pilot used the system to track pork and verify its origin and safety certificates.
- **Supplier requirement:** in 2018, Walmart announced that its fresh leafy-greens suppliers would have to trace their products using the blockchain system, after a major E. coli outbreak in romaine lettuce that year.

### 4.5 Benefits

- **Faster recalls:** the exact contaminated batch can be found in seconds, so only that batch is removed instead of all products of that kind.
- **Less food waste:** safe food no longer has to be thrown away as a precaution.
- **Fraud prevention:** fake origin claims (e.g. "organic" or a false country of origin) are much harder to make.
- **Trust and transparency:** all members share one trusted record, and customers can verify where their food came from.
- **Efficiency:** less paperwork and fewer disputes between supply-chain partners.

### 4.6 Challenges and Limitations

- **Garbage in, garbage out:** blockchain only guarantees that data is not changed **after** it is recorded. If someone enters wrong data at the start, the blockchain cannot detect it.
- **Adoption:** every party in the chain, including small farmers with limited technology, has to take part for the system to work.
- **Cost and setup:** integrating with existing systems and training staff takes time and money.
- **Governance:** competing companies must agree on rules for data sharing and access.
- **Data privacy:** companies are careful about sharing business information, even within a permissioned network.

### 4.7 Survey Conclusion

The IBM Food Trust case shows that blockchain can solve a real problem, food traceability, much better than traditional systems, cutting tracing time from days to seconds. It also shows why the **type of blockchain matters**: a permissioned consortium chain was chosen because it gives shared trust between competing companies while keeping their business data private and the system fast.

---

## 5. Challenges of Blockchain in General

- **Scalability:** public blockchains handle far fewer transactions per second than systems like Visa.
- **Energy consumption:** Proof-of-Work networks such as Bitcoin use large amounts of electricity.
- **Regulation:** laws on cryptocurrencies and blockchain differ by country and are still changing.
- **Irreversibility:** mistaken or fraudulent transactions cannot be undone.
- **Smart contract bugs:** code cannot be changed after deployment, so bugs can be exploited (e.g. the 2016 DAO hack on Ethereum).
- **Key management:** if a user loses their private key or seed phrase, their assets are lost permanently.
- **Interoperability:** different blockchains often cannot communicate with each other easily.

---

## 6. Future Scope

- Wider use of energy-efficient consensus such as Proof of Stake
- **Layer-2 solutions** (rollups) to make public blockchains faster and cheaper
- **Central Bank Digital Currencies (CBDCs)**, such as India's **e-Rupee** pilot by the RBI
- Blockchain combined with IoT and AI for automated, trusted data
- Government services such as land records, certificates and identity on blockchain
- Interoperability protocols that connect different blockchains

---

## 7. Conclusion

Blockchain is a distributed, immutable and secure ledger technology that removes the need for a central trusted authority. Depending on who may join and validate, blockchains are **public, private, consortium, or hybrid**, and each type suits different needs: public chains for open cryptocurrencies and DeFi, private chains for internal company records, consortium chains for industry collaboration, and hybrid chains for regulated sectors that need both privacy and public verification.

The survey of **IBM Food Trust and Walmart** shows that blockchain gives real, measurable benefits, reducing food traceability time from about 7 days to 2.2 seconds. Challenges such as scalability, regulation and adoption remain, but blockchain is steadily moving from cryptocurrency into finance, supply chain, healthcare, government and many other areas.

---

## References

1. S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008. https://bitcoin.org/bitcoin.pdf
2. Ethereum Foundation, "Intro to Ethereum." https://ethereum.org/en/developers/docs/intro-to-ethereum/
3. Hyperledger Foundation, "Hyperledger Fabric." https://www.hyperledger.org/projects/fabric
4. IBM, "IBM Food Trust." https://www.ibm.com/products/supply-chain-intelligence-suite/food-trust
5. GeeksforGeeks, "Types of Blockchain." https://www.geeksforgeeks.org/types-of-blockchain/
6. Lab Practice III Lab Manual, Department of Computer Engineering.
