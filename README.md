###Conway's Game of Life

The GOL is an environment where cells live and die depending on the numbers of their neighbours.

This is interesting to me for two reasons:

- Given an arrangement of cells in any large number, it would be almost impossible for a human to determine what would happen on the board
- The universe they create is entirely deterministic and the sequence for any pattern will always be the same

I have read that making the simple glider shape is a code interview question, so here it is:

![glider pic](gifs/glider.gif)

And I've also implemented more complex shapes.

![brain pic](gifs/brain.gif)

All of these shapes in the ```maps/``` folder were downloaded from this [online repository](http://www.bitstorm.org/gameoflife/lexicon/), where you can download every other known GOL shape in a ```.cells``` file.

###Installation

This guide will work on an Ubuntu machine, and possibly other OS, but I can't be certain.

Clone this repository to your computer:

    git clone https://github.com/JasonThomasData/game_of_life

Navigate to that root folder.

Get virtualenv with these commands:

    sudo apt-get update
    
    sudo apt-get install python-virtualenv

Now, install a virtualenv in the root folder:

    virtualenv -p python3 env

Activate that virtualenv:

    source env/bin/activate

Get pip3 to install dependencies:

    pip3 install -r requirements.txt

By the way, there is only one dependency there, but using requirements.txt is a good habbit. Alternatively, do:

    pip3 install numpy

###Usage

Let's suppose we want to load the glider.cells map. Do:

    python3 run_app.py maps/glider.cells

That will open a window with the animation in it. You can close that animation at the window or by doing ```ctrl+c``` from the terminal.

If you want to change the animation, change the properties of the animation class in the application folder.

###Tests

To run the tests, stay in the root folder. Do:

    python3 -m unittest discover test/

###Discussion

There are two things about this project I would like to change if I get time:

- The Animation class has details about square width and animation speed. The Board class has details about the buffer around the uploaded shapes. It would be better to have those detals passed to them from the ```run_app```. Then we could allow the user to declare those properties at the command line. It would just make a lot of sense to have ```run_app``` as the single point of user interface.

- Also at the terminal, I would add an option to generate cells randomly on the board, as that would be interesting to have random data.

This project may be great for a machine learning project, to see what arrangement can get the best outcome in terms of the most interesting results or the longest running game. To do that, I think a reinforcement learning algorithm or nueral network would do the trick.

I made this project with Python3, Ubuntu 16.04 and Vim.

###Licence

This project is in the Public Domain, and is free from copyright.

###Contributing

I did this project because:

- I knew it would be a fun program to make

- Making a glider is a code test interviewers ask

So I think you should make your own implementation of GOL since it's fun to do.

