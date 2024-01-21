# Watery Wordplay Wreck

Welcome to my third milestone project, Watery Wordplay Wreck.

Watery Wordplay Wreck is a word-guessing game built with Python. It is a <a href="https://en.wikipedia.org/wiki/Hangman_(game)" target="_blank">Hangman</a> inspired game in the style of a sinking ship to represent the progress of the game.

The user can choose the number of lives per game to set the difficulty. Through the process of making guesses, either letter by letter or by attempting to guess the entire word, the user endeavors to identify the correct word before the ship succumbs to the depths of the sea. With each unsuccessful attempt, the user loses a life, resulting in the gradual sinking of the ship.

The primary objective of this project is to showcase my comprehension and application of the Python modules I have studied thus far. By integrating them into a real-world project, I aim to demonstrate my proficiency in design and development. This terminal application, constructed using a template provided by <a href="https://github.com/Code-Institute-Org/p3-template" target="_blank">Code Institute</a> along with my Python code, serves as a tangible representation of my acquired skills.

I appreciate you taking the time to explore my project, and I sincerely hope you find as much enjoyment in it as I did during the design and development phases.

<a href="https://watery-wordplay-wreck-5dedc8ac41c5.herokuapp.com/" target="_blank">View the live project</a>

<a href="https://github.com/HCaldwell95/watery-wordplay-wreck" target="_blank">View the GitHub repository here</a>

<em>Note: While developing this project, I recognised shortcomings in my demonstration of version control. To address this, I have reconstructed the repository, ensuring proper version control practices are now in place. You can find a link to the previous repository <a href="" target="_blank"> here</a>.</em>




## UX - User Experience Design

### User Stories

As a first-time user:
  - I would like to understand how the game works and how to play with ease.
  - I would like the flexibility to tailor the difficulty to match my skill and comfort.
  - I would like prompt feedback for every guess I make during the gameplay.
  - I would like visibility of any letters or words previously used to avoid using them again.
  - I expect to receive an error message with an explanation if my guess is deemed invalid.
  - I wish to monitor my progress throughout the game.
  - I would like the option to either replay the game or conclude my session once the game concludes.

As a returning user:
  - I would like to be able to relearn the game quickly and easily.
  - I would like the challenge to remain and encounter different words than my last visit.

## Logic Flow
To organise the logical flow of the game, I created a flow chart that outlines the individual steps. Each step is color-coded to differentiate between various types of activities.

<img src="./docs/flow-chart.png" alt="Image of the project flowchart" width="700">

## Existing Features

### Welcome Page

This serves as the initial greeting for the game, featuring the game title rendered in ASCII Art. Users are prompted to initiate the game by pressing ENTER.

<img src="./docs/welcome-page.png" width="700">

---

### Rules Page

Once the user has pressed ENTER, the terminal clears and they will be taken to the Rules Page. This page consists of:
  -  A 'RULES' Title - again rendered in ASCII Art.
  -  The rules of the game and explanation of the objective.
  -  A user prompt to select their difficulty by selecting the desired number of lives.

<img src="./docs/rules-page.png" width="700">