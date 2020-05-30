# Pseudo Scrabble
Pseudo scrabble game simulation (slow with more than 5 tiles).

<br>
Initialise tile set, player, and two 'games':

	game_set = TileSet()  
	game_set.shuffle_tiles()  
	gamer = Hand()  
	gamer.label = "Patrick"  
	game_set.hand_out(gamer, 4) # provide gamer and number of tiles 
	print(gamer)  
	print(gamer.get_tiles())   
	gamer.find_words(game_set.get_tile_values()) # pseudo game 1  
	print(gamer)   
	game_set.hand_out(gamer, 2)  
	print(gamer.get_tiles())  
	gamer.find_words(game_set.get_tile_values())  pseudo game 2 
	print(gamer)

<br>
Program output:

	Patrick: ; Score: 0
	['f', 'x', 'e', 'e']
	Patrick: ex; Score: 9
	['f', 'e', 'f', 'o']
	Patrick: ex, off; Score: 18

	Process finished with exit code 0



