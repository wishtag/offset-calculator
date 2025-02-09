Offset Calculator
=====
A python program to help you hit the correct frame for RNG manipulation

I am aware there are spreadsheets out there with the delay you should use for each route or area, but I didn't want to look through spreadsheets so I just made this

Usage
=====
For this example I'm going to be using Pokémon FireRed on emulator

So you do all your other rng stuff and you find out you'll find a shiny encounter on this advance.  
![1](img/1.png?raw=true)  
So you create a savestate and then wait. You use sweet scent the exact advance that it says will give you a shiny, but instead you get the wrong Pokémon.  
![2](img/2.png?raw=true)  
From here you take the stats of the Pokémon you encountered to figure out what frame you actually hit.  
![3](img/3.png?raw=true)  
Now that you have the frame you were aiming for and the frame that you hit, you throw them into this program.  
![4](img/4.png?raw=true)  
It calculates the difference and then gives you the adjusted frame that you should aim to hit instead.  
So you go back to your game, reload to that savestate you hopefully created, and try and use sweet scent on this new frame.  
![5](img/5.png?raw=true)  
And voilà you hit the encounter you were aiming for!