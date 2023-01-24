# Loawa_Filtering_Project
### This is a simple web application that let's the user filter out top Lost Ark players on the Korean server based on their class and engravings

<img src="images/WebApp_photo.PNG" width="500"/>

Lost Ark is a Korean MMORPG that has been published and distrubted in the west by Amazon Games Studio. Currently, the western release of the game is behind in terms of content compared to the Korean version of the game, so many players in the west look to top players on the KR server for different builds and character setups. 

Loawa is a fanmade website that contains the data of every top character on the KR server, allowing users to see the different aspects of the characters such as skills, engravings, gems, etc. Because the korean version of the game is ahead of the western version, Loawa becomes a great resources for western players to see what the optimal/meta builds are for different classes based on the top players on the KR server.

## The Inspiration and Issue
I sometimes like to use Loawa to look at what the common builds are for certain classes. One day I had an idea for an engraving setup for one of the classes I play, and I wanted to see if any of the top players in Korea used a similar build.

However, the issue with Loawa is that when it comes to filtering out top characters, the filtering is limited by class. You cannot filter characters based on engravings, skills, gems, etc. This meant that if I wanted to search for players with my particular engraving setup in mind, I'd have to go through every player one-by-one and see if they had the setup that I was looking for. This was the main prompt that inspired me to make this project; an application that allowed the user to filter out top players on the Korean version of the game with more filtering options that are not available on the Loawa website.

## The Process


### 3. Added in a Shadow Tetrimino
   - The previous version didn't have a shadow tetrimino. Adding this in helps players see exactly where their tetrimino will fall
### 4. Added in a Fast Drop action
   - Pairing this with the added shadow tetrimino leads to the potentially for very fast gameplay
### 5. Added in a Holding Tetrimino function
   - With the addition of the holding piece function, players have a lot more flexibility with what tetrimino they play with. This addition in conjunction with both the new randomization and
   the extended queue make for a very modernized feel to the game.
   
#### Bug Fixes
- Fixed a bug that caused tetriminos to fly off the sides at the top of the grid if moved too quickly to the left or right at the beggining of play
- Fixed a bug that caused the game to crash if a tetrimino tried to move outside of the grid
- Fixed an issue with the tetriminos not being the correct color after the randomization changes
- Fixed a bug that caused empty rows to float when certain combinations of complete rows were deleted.
