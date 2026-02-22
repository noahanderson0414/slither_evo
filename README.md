# Slither.evo

## Installation
This repository uses Poetry for package management.
Installing the repository consists of installing Poetry
and cloning the repository. Then, you can install all of the
Poetry dependencies by running `poetry install --no-root`.

> [!NOTE]
> You can find more info for
> how install Poetry [here](https://python-poetry.org/docs/).

## Usage
Running Slither.evo is simple:
just run `poetry run python .`
in your shell.

> [!NOTE]
> You can also add the Poetry venv to the
> `VIRTUAL_ENV` environment variable and run
> Python normally.

## Features
- [-] Player controlled character
- [-] Non-player controlled characters
- [-] Slither.io-like movement
- [-] Collectible food randomly populated on map which give you points for upgrades
- [-] Level-based upgrades for player, e.g. speed, size, etc.
- [-] Species for enemies with specific characteristics
- [-] Start game with defined number of enemies, once won prompt player if they want a progressively harder endless mode
- [-] Player controlled color of character
- [-] Score when you win
- [-] All characters are killed by Tron rules (colliding with head)
- [-] More and more enemies spawn as time goes on

## Optional Features
- [-] AI-controlled character
- [-] Automatic size growth independent from upgrades
- [-] Multiplayer
- [-] Scoreboard
- [-] Multiple map sizes
