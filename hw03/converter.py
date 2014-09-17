def xorStrings(string1, string2):
	outString = ""

	for i in xrange(len(string1)):
		outString += str(int( bool(int(string1[i])) != bool(int(string2[i])) ))

	return outString

allWords =  ["ehlite", "either", "errite", "heeler", "heller", "herile", "hersir", "hetter", "hiller", "hillet", "hirsel", "hirsle", "hisser", "histie", "hither", "hitter", "illess", "illish", "iritis", "issite", "keeker", "keeler", "keelie", "kelter", "kerrie", "kerril", "kettle", "kiekie", "killer", "kilter", "kiltie", "kirker", "kirtle", "kisser", "kitish", "kittel", "kitter", "kittle", "lerret", "lessee", "lesser", "letter", "lierre", "lisere", "listel", "lister", "litter", "little", "reeker", "reeler", "reesle", "reetle", "reheel", "reiter", "rekill", "rekiss", "relier", "relish", "relist", "rereel", "rerise", "reseek", "resell", "resile", "resist", "rester", "restes", "restir", "restis", "retell", "retest", "retier", "retile", "retill", "retire", "retree", "retter", "rillet", "risker", "rissel", "risser", "rissle", "seeker", "seesee", "seethe", "seller", "sellie", "series", "sestet", "setier", "settee", "setter", "settle", "shekel", "shiest", "shriek", "shrike", "shrill", "shrite", "silker", "silkie", "siller", "siress", "sirree", "sister", "sistle", "sittee", "sitter", "skilts", "skiter", "skrike", "stilet", "streek", "streel", "street", "streke", "stress", "strike", "teerer", "teeter", "teethe", "tehsil", "tellee", "teller", "terete", "terret", "tessel", "testee", "tester", "testes", "testis", "tether", "tetter", "theirs", "theist", "theres", "theses", "thesis", "thirst", "thresh", "thrill", "tierer", "tikker", "tiller", "tilter", "tirret", "tither", "titler", "titter", "tittie", "tittle", "triker", "trikir", "trilit", "trilli", "tsetse"]

for guess in allWords:

	# pt1 = "khhltk"
	# pt2 = "kthlle"
	pt1 = "kthlle"
	pt2 = "khhltk"

	toBinary = {
		"e": "000",
		"h": "001",
		"i": "010",
		"k": "011",
		"l": "100",
		"r": "101",
		"s": "110",
		"t": "111"
	}

	fromBinary = {
		"000": "e",
		"001": "h",
		"010": "i",
		"011": "k",
		"100": "l",
		"101": "r",
		"110": "s",
		"111": "t",
	}

	key = ""
	for i in xrange(len(guess)):
		# print letter,
		key += fromBinary[xorStrings(toBinary[guess[i]], toBinary[pt1[i]])]


	otherGuess = ""
	for i in xrange(len(guess)):
		otherGuess += fromBinary[xorStrings(toBinary[pt2[i]], toBinary[key[i]])]

	# print otherGuess

	if otherGuess == "strike" or otherGuess == "shriek":
		print otherGuess, key, guess

		# for letter in key:
			# print toBinary[letter],
		# print

# actualKey = ""

# for i in xrange(0, len(key), 3):
# 	actualKey += fromBinary[key[i:i+3]]

# print actualKey

# for i in xrange(len(guess)):

