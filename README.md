# Αξιοποίηση κοινωνικών δικτύων για την μελέτη των ηλεκτρονικών μέσων ενημέρωσης



![enter image description here](https://raw.githubusercontent.com/sakis475/thesis-A.-Piplikatsis/master/pinakesArxikh.png)



## Εφαρμογή
Το παρών εγχείρημα προσπαθεί να εντοπίσει κατά πόσο τα ειδησεογραφικά στην Ελλάδα ακολουθούν τις τάσεις στο Twitter της Ελλάδας αλλά και το αντίστροφο. Οι τάσεις του Twitter αντικατοπτρίζουν όλες τις συζητήσεις που γίνονται γύρω από κάποια θέματα της επικαιρότητας. Με λίγα λόγια, μας φανερώνουν τι συζητιέται σε πανελλαδικό επίπεδο κάθε χρονική στιγμή. Έχοντας αυτή την πληροφορία διαθέσιμη καθίσταται δυνατό με τη χρήση μηχανικής μάθησης να βρεθούν για κάθε μία τάση τα αντίστοιχα άρθρα από τα ειδησεογραφικά. Έτσι δημιουργούνται συσχετίσεις μεταξύ των τάσεων του Twitter και των άρθρων από τα ειδησεογραφικά, σε σχέση πάντα με αυτά που γράφουν και οι δύο πλευρές.

Η εφαρμογή που δημιουργήθηκε είναι σε μορφή ιστοσελίδας οπότε είναι διαθέσιμη μέσω της χρήσης φυλλομετρητή (browser). Εφόσον ο server NodeJS, η βάση δεδομένων MongoDB και ο python αλγόριθμος εκτελούνται στο σύστημα τότε η εφαρμογή θα ακούει (listens) σε μία συγκεκριμένη διεύθυνση URL στον φυλλομετρητή. Αν εκτελεστεί σε τοπικό σύστημα τότε η διεύθυνση πιθανός να είναι η “localhost” ή η τοπική διεύθυνση του συστήματος. Η θύρα που είναι διαθέσιμη η ιστοσελίδα έχει οριστεί στην “5000”. Οπότε στο σύνολο της η διεύθυνση URL της εφαρμογής εδώ, είναι η “ http://localhost:5000 ” .

## Εγκατάσταση

Για την εγκατάσταση της εφαρμογής και όλων των απαιτήσεων της είναι απαραίτητη η εγκατάσταση της Docker πλατφόρμας καθώς και σύνδεση στο διαδίκτυο. Η Docker πλατφόρμα είναι διαθέσιμη για Windows, Mac και Linux. Εφόσον εγκατασταθεί και εκτελείται στο σύστημα πηγαίνουμε στον φάκελο που βρίσκεται το αρχείο docker-compose-example.yml και το μετονομάζουμε σε docker-compose.yml . Σε αυτό το αρχείο έχουν ήδη εισαχθεί οι IP διευθύνσεις, αν στο δικό σας σύστημα δεν δουλεύει με αυτές τις διευθύνσεις τότε πρέπει να τις αλλάξετε με αυτές την IP διεύθυνση του docker-engine σας.

Στην περίπτωση που είναι διαφορετική η IP διεύθυνση σας, στην μεταβλητή subnet βάζουμε την τοπική IP διεύθυνση του docker-engine, και για όλα τα containers (nodeserver, mongodb, pythonscript) στη μεταβλητή ipv4_address εισάγουμε την IP διεύθυνση με αυτή του subnet (Σ.τ.Σ. κάθε IP container πρέπει να έχει διαφορετικό HOST ID, δηλαδή το τελευταίο νούμερο της IP διεύθυνσης).
Στην συνέχεια, στο αρχείο nodeServer/config/config.env πρέπει να αλλάξετε το κομμάτι της IP στην μεταβλητή MONGO_URI με αυτή που εισάγετε στο container mongodb.
Το ίδιο πρέπει να γίνει για την μεταβλητή DATABASE_URL στο αρχείο python/dev.env
Τέλος πρέπει να εισαχθούν τα δικά σας κλειδιά για το Twitter API, στο αρχείο python/getTweets/searchTweets.py και python/getTopHashtags/getLiveTrends.py στις παραμέτρους

	auth = tweepy.OAuthHandler("your_consumer_key","your_consumer_secret")
	auth.set_access_token("your_key","your_secret")

Πλέον το μόνο που πρέπει να γίνει είναι να εκτελεστεί η εντολή

	docker-compose up

στο φάκελο που υπάρχει το αρχείο docker-compose.yml μέσω του terminal και σύντομα (μπορεί να πάρει κάποια λεπτά) αφού εγκατασταθούν (αυτόματα) όλα τα κομμάτια της εφαρμογής, η εφαρμογή θα τρέχει στην IP και θύρα localhost:5000 (αν το σύστημα είναι τοπικό).

Η εξαγωγή αποτελεσμάτων γίνεται αυτόματα και δεν χρειάζεται καμία ενέργεια από την πλευρά του χρήστη. Ωστόσο για να εμφανιστούν τα πρώτα αποτελέσματα θα πρέπει να αφεθεί το πρόγραμμα για κάποια χρονική διάρκεια (τουλάχιστον 2-4 ώρες, εξαρτάται από την επεξεργαστική ισχύ του Η/Υ) σε εκτέλεση ώστε να συλλεχθούν τα δεδομένα, να αναλυθούν και να αποθηκευτούν στην βάση δεδομένων. Μετά την αναμονή, θα πρέπει να εμφανίζεται η ιστοσελίδα σωστά.
