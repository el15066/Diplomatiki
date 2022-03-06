

# Κεφ 3: Αρχιτεκτονική και υλοποιήσεις \\\\λογισμικού για Ethereum

## Δομή Ethereum

### World state

Μιας και το Ethereum χρησιμοποιεί ledger βασισμένο σε λογαριασμούς (αντί για UTXO όπως το Bitcoin),
χρειάζεται να διατηρεί μια συνεπή (consistent) και αντιγραφόμενη (replicated) δομή με την κατάσταση (World State) των
λογαριασμών, συμβολαίων και του αποθηκευτικού χώρου των συμβολαίων (contract storage ή απλά storage).
Αυτή η δομή πρέπει να είναι και επαληθεύσιμη, να μπορεί δηλαδή να δημιουργηθεί κρυπτογραφική απόδειξη
των περιεχομένων της, η οποία απόδειξη να βρίσκεται μέσα στις επικεφαλείδες (headers) των block.
Για την επίτευξη αυτού χρησιμοποιήται η δομή modified Merkle Patricia Trie.

#### modified Merkle Patricia Trie (mMPT ή MPT)

Η δομή αυτή ορίζεται αναλυτικά στο Υellowpaper του Ethereum [@YP].
Είναι για δενδρική δομή, η οποία λειτουργεί ως Key-Value store.
Οι τιμές (Value) αποθηκεύονται στους κόμβους διακλάδωσης ή στα φύλλα του δέντρου,
ενώ το κλειδί (Key) είναι το μονοπάτι από τη ρίζα στον κόμβο όπου αποθηκεύεται η αντίστοιχη τιμή.
Υπάρχουν τρία είδη κόμβων:
- Κόμβοι διακλάδωσης βάζουν 1 δεκαδικό ψηφίο στο κλειδί.
- Κόμβοι επέκτασης βάζουν περισσότερα ψηφία.
- Κόμβοι φύλλα κρατάνε τιμές.
Επίσης επιτρέπεται και οι κόμβοι διακλάδωσης να έχουν τιμή.
Οι ακμές του αποτυπώνονται με τον κατακερματισμό (hash) των κόμβων, όχι απλά με δείκτες - διευθύνσεις μνήμης.
Επομένως, το hash της ρίζας (root hash) εξαρτάται από hash όλων των κόμβων και των τιμών του,
το οποίο επιτρέπει την (πιθανολογική) επιβεβαίωση των περιεχομένων ολόκληρης της δομής απλά συγκρίνοντας το root hash.
Το root hash τοποθετείται στην επικεφαλίδα του αντίστοιχου block.
Υπάρχουν και άλλα πλεονεκτήματα και δυνατότητες που προσφέρει η δομή αυτή, τα οποία είναι ? out of scope ?.

#### Λογαριασμού (*Accounts*)

Το Υellowpaper περιγράφει το World State ως αντιστοίχιση διευθύνσεων (addresses) σε καταστάσεις λογαριασμών (account states, εδώ απλά λογαριασμοί ή accounts).
Οι λογαρισμοί (accounts) είναι τετράδες: `(nonce, balance, storageRoot, codeHash)`.
Η αντιστοίχιση γίνεται με το MPT, με το κλειδί να είναι η διεύθυνση του account (160-bit) και η τιμή είναι ο λογαριασμός (η τετράδα).

#### Συμβόλαια (*Contracts*)

Το πεδίο `codeHash` καθορίζει αν ο λογαριασμός πρόκειται για έξυπνο συμβόλαιο (contract).
Στην περίπτωση που είναι το hash της κενής συμβολοσειράς - `HASH(())`, ο λογαριασμός είναι εξωτερικός (Externally Operated Account - EOA) και ανήκει πιθανώς σε κάποιον χρήστη.
Σε contract, το `codeHash` είναι το hash της δυαδικής κωδικοποίησης (encoding) του εκτελέσιμου κώδικά του (runtime bytecode).
Το κάθε contract έχει και μη-πτητικό (non-volatile) αποθηκευτικό χώρο (storage), με τη μορφή ζευγών:  
`slot index (32 Bytes)` $\rightarrow$ `content (32 Bytes)`  
που αποθηκεύονται ως ζεύγη key-value^[Για να αποφεύγονται επιθέσεις DOS στη δομή του MPT, δεν αποθηκεύεται (ως key) το slot, αλλά το hash του [@SECURETRIE].] σε MPT, το root hash του οποίου αποτελεί το πεδίο `storageRoot`.


### Transaction

Οι συναλλαγές (transaction) παράγονται και υπογράφονται ψηφιακά από τους χρήστες του συστήματος, εξωτερικά απ' αυτό,
και κοινοποιούνται (broadcast) στο δίκτυο του Ethereum, με σκοπό να συμπεριληφθούν τελικά σε κάποιο block από τους miners.
Επομένως, transaction μπορούν να προέρχονται μόνο από EOA.

Σε αντίθεση, οι κλήσεις-μηνύματα (message calls) μπορούν να παραχρθούν και εσωτερικά του συστήματος κατά την εκτέλεση ενός contract.
Ένα message call μπορεί να παράξει περισσότερα ακόμα calls, όχι όμως transaction.
Σε κάθε transaction αντιστοιχεί ένα αρχικό message call το οποίο γίνεται προς το contract η διεύθυνση του οποίου
αναγράφεται στο πεδίο προορισμού (`to`) του transaction (εφόσον είναι contract).
Αυτό αποτυπώνεται και στο Σχήμα 3.1 .


\begin{figure}[!htbp]
  \centering
  \includesvg[inkscapelatex=false,width=\textwidth]{../main/Message\_Calls.svg}
  \caption{Αναπαράσταση δύο transaction και των message calls που προκαλούν.}
\end{figure}


### Δημιουργία συμβολαίων

Αν το πεδίο `to` λείπει από ένα transaction, τότε πρόκειται για (πιθανή) δημιουργία νέου contract.
Το πεδό `data` τότε ερμεινεύεται ως κώδικας ο οποίος εκτελείτε άμεσα (initialization bytecode) και δεν είναι ο κώδικας του νέου contract.
Αντιθέτως, αφότου εκτελεστεί, πρόκειται να επιστρέψει τον κώδικα του νέου contract (runtime bytecode).
(Αυτό το σχήμα επιτρέπει την αποδοτική υλοποίηση της συνάρτησης αρχικοποίησης (constructor) του contract,
μιας και χρησιμοποιήται μόνο μία φορά και θα ήταν σπατάλη αν ο κώδικάς της έμενε στο τελικό contract.)
Οι αναλύσεις που θα περιγραφούν στο υπόλοιπο μέρος της εργασίας αναφέρονται μόνο στο νέο αυτό κώδικα.
Είναι επίσης δυνατό να δημιουργηθεί ένα contract, μέσω των εντολών `CREATE`, `CREATE2` κατά τη διάρκεια εκτέλεσης άλλου contract, με το ίδιο τελικά αποτέλεσμα.

### Blockchain

Τα block αποτελούνται από δύο τμήματα: επικεφαλείδα (header) και σώμα (body).

Τα transaction τοποθετούνται στο block body σε μία απλή λίστα, αλλά ταυτόχρονα σχηματίζεται ένα MPT που τα περιέχει, το root hash του οποίου τοποθετήται στο header του block.

Τα blocks παράγονται από τους miners με μη ντετερμινιστικό τρόπο. Αυτό έχει σαν αποτέλεσμα να παράγονται σε ορισμένες περιπτώσεις ταυτόχρονα blocks τα οποία προφανώς δεν είναι συμβατά και δεν μπορούνε να μπουν και τα δύο στο blockchain.
Ο αλγόριθμος consensus επιλέγει πιο θα κρατηθεί, το/α άλλο/α όμως δεν απορρίπτονται τελείως αλλά το header τους περνάει
(προαιρετικά) σε μία λίστα `ommers` (ή `uncles`) στο body επόμενου block που θα παραχθεί. Το hash αυτής τις λίστας τοποθετήται στο header του block.
(τα transaction αυτών των block φυσικά δεν εκτελούνται)

## Δομές δεδομένων

Σε αυτή την ενότητα θα περιγραφούν οι βασικές δομές δεδομένων που χρησιμοποιούν δύο δημοφιλείς clients,
ο Go-ethereum και ο Erigon, και οι διαφορές μεταξύ τους.
Στις τις δομές του Eigon που περιγράφονται εδώ βασίζεται και η υλοποίηση που περιγράφεται στο επόμενο κεφάλαιο.

### Block

#### Υλοποίηση

Η δομή των block που περιγράφηκε προηγουμένως είναι κοινή και στους 2 client:

- Header:
```go
// Header represents a block header in the Ethereum blockchain.
type Header struct {
	ParentHash  common.Hash    `json:"parentHash"       gencodec:"required"`
	UncleHash   common.Hash    `json:"sha3Uncles"       gencodec:"required"`
	Coinbase    common.Address `json:"miner"            gencodec:"required"`
	Root        common.Hash    `json:"stateRoot"        gencodec:"required"`
	TxHash      common.Hash    `json:"transactionsRoot" gencodec:"required"`
	ReceiptHash common.Hash    `json:"receiptsRoot"     gencodec:"required"`
	Bloom       Bloom          `json:"logsBloom"        gencodec:"required"`
	Difficulty  *big.Int       `json:"difficulty"       gencodec:"required"`
	Number      *big.Int       `json:"number"           gencodec:"required"`
	GasLimit    uint64         `json:"gasLimit"         gencodec:"required"`
	GasUsed     uint64         `json:"gasUsed"          gencodec:"required"`
	Time        uint64         `json:"timestamp"        gencodec:"required"`
	Extra       []byte         `json:"extraData"        gencodec:"required"`
	MixDigest   common.Hash    `json:"mixHash"`
	Nonce       BlockNonce     `json:"nonce"`

	// BaseFee was added by EIP-1559 and is ignored in legacy headers.
	BaseFee *big.Int `json:"baseFeePerGas" rlp:"optional"`
}
```


- Body:
```go
type Body struct {
	Transactions []*Transaction
	Uncles       []*Header
}
```


### State

#### Go-ethereum

Ο client go-ethereum χρησιμοποιεί εσωτερικά τη δομή MPT όπως περιγράφηκε.
Οι ακμές στο δέντρο υλοποιόνται εντός μνήμης (in-memory) με διευθύνσεις μνήμης, αλλά για να αποθηκευτούν χρειάζεται εναλλακτική μέθοδος. Αυτό γίνεται, χρησιμοποιώντας τα hash των κόμβων του δέντρου. Πιο συγκεκριμένα, χρησιμοποιώντας κάποια κοινή βάση δεδομένων τύπου KV-store, όπως τη LevelDB, η αποθήκευση επιτυγχάνεται θέτοντας ως τιμή τον σειριοποιημένο-κατά-RLP κόμβο και ως κλειδί το hash της τιμής. Στους ενδιάμεσους κόμβους (όχι φύλλα) η αναφορά στους κόμβους του επόμενου επιπέδου γίνεται με το hash τους.
Αξίζει να σημειωθεί ότι κάθε hash^[εκτός της ρίζας] αποθηκεύεται δύο φορές συνολικά:
- μία φορά ως κλειδί του αντίστοιχου κόμβου και
- μία φορά μέσα στη σειριοποιημένη τιμή ενός ενδιάμεσου κόμβου
Επίσης εδώ γίνεται εμφανές πως μιας και το ίδιο το MPT αποτελεί ουσιαστικά KV-store, δημιουργείται συνολικά ένα σχήμα KV-store-in-KV-store για την αποθήκευση των accounts.
Εντελώς ανάλογη είναι και η δομή για τα contract storage, με το root hash του storage-MPT του κάθε Contract να αποθηκεύεται στο αντίστοιχο account που περιγράφηκε προηγουμένως.


##### Υλοποίηση

Η δομή *stateDB* περιέχει τα *stateObjects*.
Τα *stateObject* αντιστοιχούν 1-1 σε *Account* τα οποία περιγράφουν:
```go
// StateDB structs within the ethereum protocol are used to store anything
// within the merkle trie. StateDBs take care of caching and storing
// nested states. It's the general query interface to retrieve:
// * Contracts
// * Accounts
type StateDB struct {
	db           Database
//...
	// This map holds 'live' objects, which will get modified while processing a state transition.
	stateObjects        map[common.Address]*stateObject
	stateObjectsPending map[common.Address]struct{} // State objects finalized but not yet written to the trie
	stateObjectsDirty   map[common.Address]struct{} // State objects modified in the current execution
```


Δημιουγούνται διαβάζοντας το αντίστοιχο *Account* από τη *stateDB*:
```go
// getStateObject retrieves a state object given by the address, returning nil if
// the object is not found or was deleted in this execution context. If you need
// to differentiate between non-existent/just-deleted, use getDeletedStateObject.
func (s *StateDB) getStateObject(addr common.Address) *stateObject {
	if obj := s.getDeletedStateObject(addr); obj != nil && !obj.deleted {
//...
func (s *StateDB) getDeletedStateObject(addr common.Address) *stateObject {
//...
	if s.snap != nil {
//...
		var acc *snapshot.Account
		if acc, err = s.snap.Account(crypto.HashData(s.hasher, addr.Bytes())); err == nil {
//...
	}
	// If snapshot unavailable or reading from it failed, load from the database
	if s.snap == nil || err != nil {
//...
		enc, err := s.trie.TryGet(addr.Bytes())
```


Εδώ εφαρμόζεται μία in-memory read-write cache που ονομάζεται (στον κώδικα) *snapshot*^[Αν και in-memory, μπορεί να αποθηκευτεί κατά το κλείσιμο του client στον δίσκο, ώστε να διαβαστεί κατά την εκκίνηση μελλοντικής εκτέλεσης και να μην χρειαστεί να ξανα-δημιουργηθεί.].
Έχει πολλαπλά επίπεδα (layers) τα οποία περιέχουν *Accounts* και *Storage* που έχουν ήδη διαβαστεί ή τροποποιηθεί κατά την εκτέλεση.
Η αναζήτηση γίνεται περώντας από τα επίπεδα με τη σειρά, μέχρι να βρεθεί το κλειδί (διεύθυνση *Account* ή *Storage*) που αναζητήται.
Αν δεν βρεθεί σε κανένα επίπεδο γίνεται ανάκτηση από το *Trie*.
Λόγο του μεταβλητού και εν δυνάμει μεγάλου πλήθους των layers που πρέπει να εξεταστούν για ένα κλειδί που δεν υπάρχει στο *snapshot*,
διατηρείται ένα φίλτρο Bloom, το οποίο αποφαίνεται για την πιθανή^[Σε περίπτωση που το κλειδί υπάρχει, η απάντηση είναι βέβαιη, ενώ σε περίπτωση που δεν υπάρχει, μπορεί να δοθεί ψευδώς θετική απάντηση ότι υπάρχει. Αυτή η συμπεριφορά του φίλτρου δεν επιρρεάζει την ορθότητα των αποτελεσμάτων.] ύπαρξη ή όχι του κλειδιού σε οποιοδήποτε layer, πριν ξεκινήση η αναζήτηση.
Έτσι, αρκετές άσκοπες αναζητήσεις παρακάμπτωνται.

Υλοποίηση αναζήτησης (παράδειγμα για *Account*):
```go
// Account directly retrieves the account associated with a particular hash in
// the snapshot slim data format.
func (dl *diffLayer) Account(hash common.Hash) (*Account, error) {
	data, err := dl.AccountRLP(hash)
//...
func (dl *diffLayer) AccountRLP(hash common.Hash) ([]byte, error) {
	// Check the bloom filter first whether there's even a point in reaching into
	// all the maps in all the layers below
	dl.lock.RLock()
	hit := dl.diffed.Contains(accountBloomHasher(hash))
//...
	// The bloom filter hit, start poking in the internal maps
	return dl.accountRLP(hash, 0)
//...
func (dl *diffLayer) accountRLP(hash common.Hash, depth int) ([]byte, error) {
//...
	if diff, ok := dl.parent.(*diffLayer); ok {
		return diff.accountRLP(hash, depth+1)
	}
//...
	return dl.parent.AccountRLP(hash)
```


Αν αποτύχει:
```go
// ReadAccountSnapshot retrieves the snapshot entry of an account trie leaf.
func ReadAccountSnapshot(db ethdb.KeyValueReader, hash common.Hash) []byte {
	data, _ := db.Get(accountSnapshotKey(hash))
	return data
}
```


Σε περίπτωση που το *snapshot* δεν υπάρχει (πχ δεν έχει δημιουργηθεί ακόμα) ή δεν περιέχει το κλειδί που ζητήται, η ανάκτηση γίνεται από το αντίστοιχο *state Trie*:
```go
func (t *Trie) TryGet(key []byte) ([]byte, error) {
	value, newroot, didResolve, err := t.tryGet(t.root, keybytesToHex(key), 0)
//...
func (t *Trie) tryGet(origNode node, key []byte, pos int) (value []byte, newnode node, didResolve bool, err error) {
//...
	case *fullNode:
		value, newnode, didResolve, err = t.tryGet(n.Children[key[pos]], key, pos+1)
//...
	case hashNode:
		child, err := t.resolveHash(n, key[:pos])
```


Η αναζήτηση αυτή πιθανών να προκαλέσει μία ή και παραπάνω αναγνώσεις απ'το δίσκο, με τη διαδικασία αναζήτησης που περιγράψαμε προηγουμένως.
Η υλοποίση φαίνεται παρακάτω:
```go
func (t *Trie) resolveHash(n hashNode, prefix []byte) (node, error) {
	hash := common.BytesToHash(n)
	if node := t.db.node(hash); node != nil {
```

```go
func (db *Database) node(hash common.Hash) node {
//...
	// Content unavailable in memory, attempt to retrieve from disk
	enc, err := db.diskdb.Get(hash[:])
```

```go
import (
//...
	"github.com/syndtr/goleveldb/leveldb"
//...
type Database struct {
//...
	db *leveldb.DB // LevelDB instance
//...
// Get retrieves the given key if it's present in the key-value store.
func (db *Database) Get(key []byte) ([]byte, error) {
	dat, err := db.db.Get(key, nil)
	if err != nil {
		return nil, err
	}
	return dat, nil
}
```


Τα *stateObject* ανακτούν δεδομένα *Storage* με τον ίδιο τρόπο:
```go
func (s *stateObject) GetState(db Database, key common.Hash) common.Hash {
//...
	return s.GetCommittedState(db, key)
//...
func (s *stateObject) GetCommittedState(db Database, key common.Hash) common.Hash {
//...
	if s.db.snap != nil {
//...
		enc, err = s.db.snap.Storage(s.addrHash, crypto.Keccak256Hash(key.Bytes()))
//...
	}
//...
		if enc, err = s.getTrie(db).TryGet(key.Bytes()); err != nil {
```


Οι ανακτήσεις δεδομένων *Storage* προκαλούνται από εντολές SLOAD/SSTORE κατά την εκτέλεση κάποιου *Smart Contract*:
```go
func opSstore(pc *uint64, interpreter *EVMInterpreter, scope *ScopeContext) ([]byte, error) {
	loc := scope.Stack.pop()
	val := scope.Stack.pop()
	interpreter.evm.StateDB.SetState(scope.Contract.Address(),
		loc.Bytes32(), val.Bytes32())
	return nil, nil
}

func opJump(pc *uint64, interpreter *EVMInterpreter, scope *ScopeContext) ([]byte, error) {
	pos := scope.Stack.pop()
	if !scope.Contract.validJumpdest(&pos) {
		return nil, ErrInvalidJump
	}
	*pc = pos.Uint64()
	return nil, nil
}
```


Επιπλέον ανακτήσεις, αυτή τη φορά για *Accounts*, γίνονται κατά την εκτέλεση των transaction καθώς και την ολοκλήρωση της επεξεργασίας ενός *Block*:
```go
func (p *StateProcessor) Process(block *types.Block, statedb *state.StateDB, cfg vm.Config) (types.Receipts, []*types.Log, uint64, error) {
//...
	for i, tx := range block.Transactions() {
//...
	}
	// Finalize the block, applying any consensus engine specific extras (e.g. block rewards)
	p.engine.Finalize(p.bc, header, statedb, block.Transactions(), block.Uncles())

	return receipts, allLogs, *usedGas, nil
}
```

```go
// Finalize implements consensus.Engine, accumulating the block and uncle rewards,
// setting the final state on the header
func (ethash *Ethash) Finalize(chain consensus.ChainHeaderReader, header *types.Header, state *state.StateDB, txs []*types.Transaction, uncles []*types.Header) {
	// Accumulate any block and uncle rewards and commit the final state root
	accumulateRewards(chain.Config(), state, header, uncles)
	header.Root = state.IntermediateRoot(chain.Config().IsEIP158(header.Number))
}
```

```go
func (s *StateDB) IntermediateRoot(deleteEmptyObjects bool) common.Hash {
	// Finalise all the dirty storage states and write them into the tries
	s.Finalise(deleteEmptyObjects)

	// If there was a trie prefetcher operating, it gets aborted and irrevocably
	// modified after we start retrieving tries. Remove it from the statedb after
	// this round of use.
	//
	// This is weird pre-byzantium since the first tx runs with a prefetcher and
	// the remainder without, but pre-byzantium even the initial prefetcher is
	// useless, so no sleep lost.
	prefetcher := s.prefetcher
	if s.prefetcher != nil {
		defer func() {
			s.prefetcher.close()
			s.prefetcher = nil
		}()
	}
	// Although naively it makes sense to retrieve the account trie and then do
	// the contract storage and account updates sequentially, that short circuits
	// the account prefetcher. Instead, let's process all the storage updates
	// first, giving the account prefeches just a few more milliseconds of time
	// to pull useful data from disk.
	for addr := range s.stateObjectsPending {
		if obj := s.stateObjects[addr]; !obj.deleted {
			obj.updateRoot(s.db)
		}
	}
	// Now we're about to start to write changes to the trie. The trie is so far
	// _untouched_. We can check with the prefetcher, if it can give us a trie
	// which has the same root, but also has some content loaded into it.
	if prefetcher != nil {
		if trie := prefetcher.trie(s.originalRoot); trie != nil {
			s.trie = trie
		}
	}
	usedAddrs := make([][]byte, 0, len(s.stateObjectsPending))
	for addr := range s.stateObjectsPending {
		if obj := s.stateObjects[addr]; obj.deleted {
			s.deleteStateObject(obj)
		} else {
			s.updateStateObject(obj)
		}
		usedAddrs = append(usedAddrs, common.CopyBytes(addr[:])) // Copy needed for closure
	}
	if prefetcher != nil {
		prefetcher.used(s.originalRoot, usedAddrs)
	}
	if len(s.stateObjectsPending) > 0 {
		s.stateObjectsPending = make(map[common.Address]struct{})
	}
	// Track the amount of time wasted on hashing the account trie
	if metrics.EnabledExpensive {
		defer func(start time.Time) { s.AccountHashes += time.Since(start) }(time.Now())
	}
	return s.trie.Hash()
}
```

```go
// updateStateObject writes the given object to the trie.
func (s *StateDB) updateStateObject(obj *stateObject) {
//...
	data, err := rlp.EncodeToBytes(obj)
//...
	if err = s.trie.TryUpdate(addr[:], data); err != nil {
```


Τέλος, η εγγραφή όλων των τροποποιήσεων στη βάση στο δίσκο γίνεται αργότερα, με κλήση στο *Trie*:
```go
func (t *Trie) Commit(onleaf LeafCallback) (root common.Hash, err error) {
//...
	h := newCommitter()
//...
	newRoot, err = h.Commit(t.root, t.db)
```




#### Erigon

Ο client erigon ξεκίνησε από τροποποιήσεις του κώδικα του go-ethereum (fork) με σκοπό την επιτάχυνσή του [@ERIGON], και επομένως οι δύο client έχουν πολλά κοινά κομμάτια. Κάποιες από τις διαφορές τους που αφορούν την εργασία αναλύονται παρακάτω.
Μία βασική διαφορά του είναι ο χωρισμός της συνολικής δουλειάς του σε στάδια (stages), όπως το στάδιο μεταφόρτωσης (downloading) των header και body των block, το στάδιο εκτέλεσης (execution stage) και άλλα.
Στο σχήμα 3.2 φαίνεται ενδεικτικά το ποσοστό του συνολικού χρόνου που διαρκεί το κάθε στάδιο, ενώ στο σχήμα 3.3 έχουν αφαιρεθεί τα στάδια downloading, που εξαρτώνται απ' το δίκτυο.

\begin{figure}[!htbp]
  \centering
  \includesvg[inkscapelatex=false,width=\textwidth]{../main/stagedsync\_proportions\_1.svg}
  \caption{Ενδεικτική διάρκεια των σταδίων του *Erigon*.}
\end{figure}


\begin{figure}[!htbp]
  \centering
  \includesvg[inkscapelatex=false,width=\textwidth]{../main/stagedsync\_proportions\_2.svg}
  \caption{Ενδεικτική διάρκεια των σταδίων του *Erigon*, αγνοώντας τα στάδια μεταφόρτωσης.}
\end{figure}


Η εργασία αυτή ασχολείται αποκλειστικά με το στάδιο execution, μιας και διαρκεί το μεγαλύτερο χρόνο.

Άλλη μία διαφορά είναι ο τρόπος αποθήκευσης των δεδομένων.
Ο Erigon δεν χρησιμοποιεί δομή MPT, αντιθέτως αποθηκεύει τα accounts και τα contract storage απ' ευθείας στη βάση δεδομένων, χωρίς τον υπολογισμό των αντίστοιχων hash, σε "πίνακα" (bucket) που ονομάζει "Plain State".
Για την επιβεβαίωση των root hash που βρίσκονται μέσα στα block, προστίθεται ένα επιπλέον στάδιο κατά το οποίο υπολογίζονται τα hashes (και πιο συμαντικά το root hash), μαζικά, σαν να ήταν σε μορφή MPT.

Επίσης, χρησιμοποιέι μια write-cache, βασιζόμενη σε β-δέντρα, η οποία κρατάει στη μνήμη (write-back) όλες τις εγγραφές που πρόκειται να γίνουν στη βάση, μέχρι το μέγεθός της να υπερβεί κάποιο προδιαγεγραμμένο όριο. Όταν το υπερβεί, η εκτέλεση έρχεται σε παύση, οι εγγραφές καταχωρούνται στη βάση και η cache αδειάζει. Αυτό, από πειραματικές δοκιμές φαίνεται συμβαίνει κάθε λίγες χιλιάδες block, αλλά κυμαίνεται αρκετά με βάση το περιεχόμενό τους.
Από το τρόπο λειτουργείας των β-δέντρων, η διάσχιση στην cache και καταχώρηση στη βάση γίνεται με τα κλειδιά να είναι ταξινομημένα, το οποίο αυξάνει την ταχύτητα της διαδικασίας [@SORTEDFAST].

Τέλος η βάση δεδομένων που χρησιμοποιεί είναι η MDBX [@MDBX], παράγωγο έργο από την LMDB [@LMDB], η οποία λειτουγρεί αποκλειστικά με αντιστοίχιση του αρχείου της στη μνήμη (memory mapping).
Ως εκ τούτου, η cache του συστήματος αρχείων λειτουργεί αποδοτικά και ως read cache για τον Erigon, γενονός που αξιοποιήθηκε από την παρούσα εργασία, όπως θα αναλυθεί σε επόμενο κεφάλαιο.

##### Υλοποίηση

Η οργάνωση της *State Database* του *Erigon* μοιάζει με αυτή του *Go-ethereum*, με αρκετές όμως συμαντικές διαφορές.
Βλέπουμε και εδώ τα *stateObjects* τα οποία όμως περιέχονται στη δομή *IntraBlockState*, η οποία επίσης λειτουργεί ως read-write cache.
Όπως φαίνεται και απ'το όνομά της, έχει ? SCOPE ? εντός ενός block, με την ένοια ότι
οι τροποποιήσεις κρατώνται στη δομή αυτή μόνο για τη διάρκεια ενός block.
Θα δούμε αργότερα τι γίνεται κατά την ολοκλήρωση του block.

Δομή *IntraBlockState*:
```go
// IntraBlockState is responsible for caching and managing state changes
// that occur during block's execution.
// NOT THREAD SAFE!
type IntraBlockState struct {
	stateReader StateReader

	// This map holds 'live' objects, which will get modified while processing a state transition.
	stateObjects      map[common.Address]*stateObject
	stateObjectsDirty map[common.Address]struct{}

	nilAccounts map[common.Address]struct{} // Remember non-existent account to avoid reading them again

	// DB error.
	// State objects are used by the consensus core and VM which are
	// unable to deal with database-level errors. Any error that occurs
	// during a database read is memoized here and will eventually be returned
	// by IntraBlockState.Commit.
	dbErr error

	// The refund counter, also used by state transitioning.
	refund uint64

	thash, bhash common.Hash
	txIndex      int
	logs         map[common.Hash][]*types.Log
	logSize      uint

	// Journal of state modifications. This is the backbone of
	// Snapshot and RevertToSnapshot.
	journal        *journal
	validRevisions []revision
	nextRevisionID int
	tracer         StateTracer
	trace          bool
	accessList     *accessList
}
```


Η δημιουργεία του *stateObject* γίνεται πάλι με ανάκτηση του αντίστοιχου *Account*:
```go
// Retrieve a state object given my the address. Returns nil if not found.
func (sdb *IntraBlockState) getStateObject(addr common.Address) (stateObject *stateObject) {
//...
	if obj := sdb.stateObjects[addr]; obj != nil {
//...
		return obj
//...
	}
//...
	account, err := sdb.stateReader.ReadAccountData(addr)
```


Η διαφορά γίνεται εμφανής στην ανάγνωση του *Account* μιας και εδώ δεν υπάρχει δομή *Trie*:
```go
func (r *PlainStateReader) ReadAccountData(address common.Address) (*accounts.Account, error) {
//...
	enc, err := r.db.GetOne(kv.PlainState, address.Bytes())
```


Έτσι φτάνουμε στο επίπεδο της write-back write-cache που ονομάζεται (στον κώδικα) *mutation*.
Αξίζει να σημειωθεί ότι οι αναγνώσεις πρέπει επίσης να κοιτάξουν τη write-cache μιας και μπορεί να έχει γίνει τροποποίηση που δεν έχει αποτυπωθεί ακόμα στην κύρια βάση.

```go
func (m *mutation) GetOne(table string, key []byte) ([]byte, error) {
	if value, ok := m.getMem(table, key); ok {
		if value == nil {
			return nil, nil
		}
		return value, nil
	}
	if m.db != nil {
		// TODO: simplify when tx can no longer be parent of mutation
		value, err := m.db.GetOne(table, key)
```

```go
func (m *mutation) getMem(table string, key []byte) ([]byte, bool) {
	m.mu.RLock()
	defer m.mu.RUnlock()
	m.searchItem.table = table
	m.searchItem.key = key
	i := m.puts.Get(&m.searchItem)
```

```go
import (
//...
	"github.com/google/btree"
//...
type mutation struct {
	puts       *btree.BTree
	db         kv.RwTx
```

```go
func (tx *MdbxTx) GetOne(bucket string, k []byte) ([]byte, error) {
	c, err := tx.statelessCursor(bucket)
	if err != nil {
		return nil, err
	}
	_, v, err := c.SeekExact(k)
	return v, err
}
```


Τα *stateObject* ανακτούν δεδομένα *Storage* με τον ίδιο τρόπο:
```go
// GetState returns a value from account storage.
func (so *stateObject) GetState(key *common.Hash, out *uint256.Int) {
//...
	value, dirty := so.dirtyStorage[*key]
//...
	so.GetCommittedState(key, out)
```

```go
func (so *stateObject) GetCommittedState(key *common.Hash, out *uint256.Int) {
//...
	// If we have the original value cached, return that
//...
		value, cached := so.originStorage[*key]
//...
	enc, err := so.db.stateReader.ReadAccountStorage(so.address, so.data.GetIncarnation(), key)
```

```go
func (r *PlainStateReader) ReadAccountStorage(address common.Address, incarnation uint64, key *common.Hash) ([]byte, error) {
//...
	enc, err := r.db.GetOne(kv.PlainState, compositeKey)
```


Όπως είδαμε και προηγουμένως, οι ανακτήσεις δεδομένων *Storage* προκαλούνται από εντολές SLOAD/SSTORE:
```go
func opSload(pc *uint64, interpreter *EVMInterpreter, callContext *callCtx) ([]byte, error) {
	loc := callContext.stack.Peek()
	interpreter.hasherBuf = loc.Bytes32()
	if common.DEBUG_TX && isDebugTX(interpreter) { fmt.Println(fmt.Sprintf("-%6x %20s       STORAGE %x", *pc,  "SLOAD", &interpreter.hasherBuf)) }
	interpreter.evm.IntraBlockState.GetState(callContext.contract.Address(), &interpreter.hasherBuf, loc)
	if common.DEBUG_TX && isDebugTX(interpreter) { fmt.Println("-") }
	return nil, nil
}

func opSstore(pc *uint64, interpreter *EVMInterpreter, callContext *callCtx) ([]byte, error) {
	loc := callContext.stack.PopPtr()
	val := callContext.stack.PopPtr()
	interpreter.hasherBuf = loc.Bytes32()
	// In debug, there will be 2 storage access lines before this one, caused by op.dynamicGas (see makeGasSStoreFunc)
	if common.DEBUG_TX && isDebugTX(interpreter) { fmt.Println(fmt.Sprintf("-%6x %20s       STORAGE %x #%x", *pc, "SSTORE", &interpreter.hasherBuf, val.Bytes())) }
	interpreter.evm.IntraBlockState.SetState(callContext.contract.Address(), &interpreter.hasherBuf, *val)
	if common.DEBUG_TX && isDebugTX(interpreter) { fmt.Println("-") }
	return nil, nil
}
```


Επίσης, οι ανακτήσεις για *Accounts*, που γίνονται κατά την ολοκλήρωση της επεξεργασίας ενός *Block*:
```go
func ExecuteBlockEphemerally(
//...
	for i, tx := range block.Transactions() {
//...
	}
//...
		if err := FinalizeBlockExecution(engine, stateReader, block.Header(), block.Transactions(), block.Uncles(), stateWriter, chainConfig, ibs, receipts, epochReader, chainReader); err != nil {
```

```go
func FinalizeBlockExecution(engine consensus.Engine, stateReader state.StateReader, header *types.Header, txs types.Transactions, uncles []*types.Header, stateWriter state.WriterWithChangeSets, cc *params.ChainConfig, ibs *state.IntraBlockState, receipts types.Receipts, e consensus.EpochReader, headerReader consensus.ChainHeaderReader) error {
//...
	if err := ibs.CommitBlock(cc.Rules(header.Number.Uint64()), stateWriter); err != nil {
//...
	if err := stateWriter.WriteChangeSets(); err != nil {
```

```go
	return sdb.txIndex
}

```

```go
func (w *PlainStateWriter) WriteChangeSets() error {
//...
		return w.csw.WriteChangeSets()
```


Εδώ, που πρόκειται να γίνει η οριστικοποίηση του *Block*, πρέπει να γίνουν κάποιες εγγραφές.
Οι εγγραφές αυτές θα καταλήξουν στη write-cache (*mutation*) αλλά, μιας και δεν υπάρχει η δομή *MPT* (όπως στο *go-ethereum*), η διαδικασία διαφέρει αρκετά.
Η δομή *MPT* από μόνη της έχει την ιδιότητα ότι οι εγγραφές δεν πανω-γράφουν (overwrite) τις παλιές τιμές, αλλά,
χάρη στην συνάρτηση κατακερματισμού^[Τροποποιημένα δεδομένα δίνουν τελείως διαφορετικό αποτέλεσμα κατακερματισμού (*hash*) το οποίο χρησιμοποιήται ως νέα διεύθυνση, η οποία είναι άδεια (αγνοώντας συγκρούσεις κατακερματισμού).], παράγεται νέα (κενή) διεύθυνση στην οποία αποθηκεύονται.
Αυτό δίνει τη δυνατότητα ιστορικής αναδρομής σε προηγούμενες καταστάσεις (*historic states*), απλά αλλάζοντας το *root hash*.
Χωρίς το *MPT*, για να έχει ο *Erigon* την ίδια δυνατότητα, κρατάει πίνακες στη βάση με τις τροποποιήσεις που έχουν γίνει (*change-set*).

Η ενεργοποίηση είναι προεραιτική και γίνεται στην αρχή της εκτέλεσης:
```go
func newStateReaderWriter(
//...
	if writeChangesets {
		stateWriter = state.NewPlainStateWriter(batch, tx, block.NumberU64()).SetAccumulator(accumulator)
	} else {
		stateWriter = state.NewPlainStateWriterNoHistory(batch).SetAccumulator(accumulator)
	}
```


Αν ενεργοποιηθεί, οι εγγραφές γίνονται με τον *change_set_writer*:
```go
func (w *ChangeSetWriter) WriteChangeSets() error {
//...
	accountChanges, err := w.GetAccountChanges()
//...
	if err = changeset.Mapper[kv.AccountChangeSet].Encode(w.blockNumber, accountChanges, func(k, v []byte) error {
//...
		if err = w.db.AppendDup(kv.AccountChangeSet, k, v); err != nil {
//...
	storageChanges, err := w.GetStorageChanges()
//...
	if err = changeset.Mapper[kv.StorageChangeSet].Encode(w.blockNumber, storageChanges, func(k, v []byte) error {
//...
		if err = w.db.AppendDup(kv.StorageChangeSet, k, v); err != nil {
```


Η συνάρτηση *Encode()* κάνει απλή μετάφραση και ταξινόμηση:
```go
func EncodeAccounts(blockN uint64, s *ChangeSet, f func(k, v []byte) error) error {
	sort.Sort(s)
	newK := dbutils.EncodeBlockNumber(blockN)
	for _, cs := range s.Changes {
		newV := make([]byte, len(cs.Key)+len(cs.Value))
		copy(newV, cs.Key)
		copy(newV[len(cs.Key):], cs.Value)
		if err := f(newK, newV); err != nil {
			return err
		}
	}
	return nil
}
```

(υπάρχει και αντίστοιχη για *Storage*)

Η συνάρτηση *AppendDup()* είναι ισοδύναμη με την *Put()* στο *mutation* που είδαμε προηγουμένως.
```go
func (m *mutation) AppendDup(table string, key []byte, value []byte) error {
	return m.Put(table, key, value)
}
```



## EVM

#### Μοντέλο εκτέλεσης transaction

μοντέλο εισόδου-εξόδου, μνημών, εξαιρέσεων
μοντέλο επεξεργασίας, αρχιτεκτονική στοίβας

#### Προγραμματισμός SC σε υψηλό επίπεδο - Solidity

βασικά για solidity lang
έξοδος του compiler (creation, runtime)
δομή του runtime εκτελέσιμου
- dispatch - μέθοδοι και κλήσεις
- 'τακτοποίηση' δεδομένων σε μόνιμη μνήμη του contract

