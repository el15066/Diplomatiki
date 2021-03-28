
# Related work

## Βελτιστοποίηση Blockchain sync

### Concurency

#### Ethereum

##### [An Empirical Study of Speculative Concurrency in Ethereum Smart Contracts](https://arxiv.org/abs/1901.01376)
Αυτό ήταν το πρώτο paper. Χρησημοποίησαν transaction από διάφορες χρονικές περιόδους εντός του 2016 και 2017, τις οποίες κάνουν replay με 16/32/64 "thread" παράλληλα. Τα transactions που έχουν conflict γίνονται rolled back και αφήνονται για μεταγενέστερη εκτέλεση σειριακά. Οι μετρήσεις γίνονται σε gas used (~ αριθμό instructions) του EVM (Ethereum virtual machine) γιατί δεν τρέχουν σε πραγματικό multi-threaded EVM αλλά σε προσομοίωση, απ'ότι κατάλαβα.

##### [On transaction parallelizability in Ethereum](https://arxiv.org/abs/1901.09942)
Αυτό υποθέτει ότι υπάρχει ήδη γνώση για '[access lists](https://github.com/ethereum/sharding/blob/master/docs/doc.md#access-list)', λίστες που δείχνουν σε τι θέσεις μνήμης μπορεί να έχει πρόσβαση το κάθε transaction - (έχουν προταθεί αλλά δεν έχουν υλοποιηθεί ακόμα, μάλλον θα υπάρχουν στο Ethereum 2.0). Δοκιμάζει 2 schedulers που εγγυόνται ότι δεν θα υπάρχουν conflict. Οι μετρήσεις και εδώ γίνονται σε gas used (άρα ανεξάρτητες απ'το hardware). Συμαντική διαφορά με το προηγούμενο ότι δεν γίνονται roll-back.

###### [Parallelilizing EVM through end-of-the-block virtual transactions](https://ethresear.ch/t/parallelilizing-evm-through-end-of-the-block-virtual-transactions/7787) (forum)
Μία άλλη μέθοδος που χωρίζει τα transactions σε νέα εικονικά, όταν καλείται κάποιο 3ο contract. Δεν δίνονται παραπάνω λεπτομέρειες/νούμερα κτλ. Γενικά μου φαίνεται παρόμοιο με το να έχει lock σε κάθε κλήση.

Γενικώς με το θέμα της παραλληλοποίησης, δεν γνωρίζω τι επίπτωση θα έχει το Eth 2.0 όταν φτάσει (~ τέλος 2021, αρχές 2022), το οποίο θα περιέχει [sharding](https://ethereum.org/en/eth2/shard-chains/), με τις λεπτομέρεις να είναι ακόμα υπό εξέταση (πχ αν θα έχει access list).

#### Hyperledger

##### [FastFabric: Scaling Hyperledger Fabric to 20,000 Transactions per Second](https://arxiv.org/abs/1901.00910)
TODO

---

### Memory/storage

#### [Turbo-geth](https://github.com/ledgerwatch/turbo-geth)
[Γενική σύντομη εισαγωγή](https://github.com/AlexeyAkhunov/papers/blob/master/Turbo-Geth-Silkworm.pdf)

##### Talks
Γενικώς το εισαγωγικό documentation που μπόρεσα να βρω είναι σε ομιλίες με τα αντίστοιχα slide.
Είναι αρκετά κομμάτια που επαναλλαμβάνονται από ομιλία σε ομιλία οπότε θέλει skip σε κάποια σημεία.

11 Dec 2018 - Turbo-Geth: optimising Ethereum clients by Alexey Akhunov, [Youtube](https://www.youtube.com/watch?v=CSpc1vZQW2Q), [Slides](https://github.com/AlexeyAkhunov/papers/blob/master/TurboGeth-Devcon4.pdf)

14 Oct 2020 - Turbo-Geth - too good to be true?, [Youtube](https://www.youtube.com/watch?v=aAZoiJIQiTE), [Slides](https://github.com/AlexeyAkhunov/papers/blob/master/Turbo-Geth-too_good_to_be_true.pdf)

12 Nov 2020 - Turbo Geth: What is it all about?, [Youtube](https://www.youtube.com/watch?v=oEpY4NkkeYQ), [Slides](https://github.com/AlexeyAkhunov/papers/blob/master/Turbo-Geth-what-is-it-about-now.pdf)

###### Stages

Γενικά για τη χρήση του δίσκου και τα στάδια που εκτελεί όταν κάνει συγχρονισμό:  
https://ledgerwatch.github.io/turbo_geth_release.html#Disk-space  
https://ledgerwatch.github.io/turbo_geth_release.html#Staged-sync  
Νεότερο:  
https://github.com/ledgerwatch/turbo-geth/blob/master/eth/stagedsync/README.md

###### Data model
DB: https://github.com/ledgerwatch/turbo-geth/blob/master/docs/programmers_guide/db_walkthrough.MD  
Research: https://ledgerwatch.github.io/Ethereum_1_Research_topics.html#Flat-data-layout-for-storing-the-state

Εδώ έχουν θέματα που είναι under development:
https://github.com/ledgerwatch/turbo-geth/wiki/Turbo-Geth-(Silkworm)-projects


##### Stateless ethereum (δεν έχω κοιτάξει ακόμα)

https://blog.ethereum.org/2019/12/30/eth1x-files-state-of-stateless-ethereum/
https://github.com/ethereum/stateless-ethereum-specs
https://medium.com/@mandrigin/semi-stateless-initial-sync-experiment-897cc9c330cb
https://ledgerwatch.github.io/Ethereum_1_Research_topics.html#Stateless-Ethereum
Turbo-Geth and Stateless Ethereum, [Youtube](https://www.youtube.com/watch?v=3-Mn7OckSus), [Slides](https://github.com/AlexeyAkhunov/papers/blob/master/Turbo-Geth_Stateless-Ethereum_EthCC-2020.pdf)


### [Tests](https://github.com/el15066/Diplomatiki/tree/main/bc_sync/test)

---

## Blockchain marketplace

### TODO

[Securing NATted IoT Devices Using Ethereum Blockchain and Distributed TURN Servers](https://www.researchgate.net/publication/332377235_Securing_NATted_IoT_Devices_Using_Ethereum_Blockchain_and_Distributed_TURN_Servers)  
[Rewarding Relays for Decentralised NAT Traversal Using Smart Contracts](https://www.ee.ucl.ac.uk/~gpavlou/Publications/Conference-papers/Keizer-20.pdf)  
[CloudAgora: Democratizing the Cloud](http://www.cslab.ece.ntua.gr/~doka/paper/cloudAgora.pdf)  
[Building Ad-Hoc Clouds with CloudAgora](http://www.cslab.ece.ntua.gr/~doka/paper/cloudAgora_demo.pdf)  
[Leveraging Blockchain Technology to Break the Cloud Computing Market Monopoly](https://www.mdpi.com/2073-431X/9/1/9)  

---
