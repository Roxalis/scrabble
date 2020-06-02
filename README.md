# Pseudo Scrabble
Pseudo scrabble game simulation.

<br>
Initialise tile set, player, and two 'games':

	game_set = TileSet()
	game_set.shuffle_tiles()
	gamer = Hand()
	gamer.label = "Patrick"
	game_set.hand_out(gamer, 7)
	print(gamer)
	print(gamer.get_tiles())
	gamer.find_words(game_set.get_tile_values())
	print(gamer)
	game_set.hand_out(gamer, 7 - len(gamer.get_tiles()))
	print(gamer.get_tiles())
	gamer.find_words(game_set.get_tile_values())
	print(gamer)

<br>
Program output:

	Patrick: ; Score: 0
	['h', 'm', 's', 'b', 't', 'i', 'r']
	Patrick: mirths; Score: 11
	['b', 'a', 'b', 'z', 'l', 'a', 'e']
	Patrick: mirths, ablaze; Score: 28

	Process finished with exit code 0



