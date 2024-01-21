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

---

### Game Page

Upon selecting the preferred number of lives, the game commences. Each session introduces a randomly chosen nautical-themed word, presenting a sinking ship image that dynamically reflects the remaining lives. The screen consistently displays the number of letters in the secret word.

At the bottom of the page, the user is prompted to input either a letter or a word.

<img src="./docs/game-page.png" width="700"> 

<br>

Each user input undergoes validation checks to determine its presence in the word or if it matches the actual word. If the user's input is found in the word, constructive feedback is provided. The revealed letter appears in the "The word to guess" field, aiding the user in tracking the word's progress.

<img src="./docs/correct-guess.png" width="700">

<br>

If the user's input is not part of the word, feedback is shared, along with the remaining lives count. With each unsuccessful attempt, the user loses a life, and the ship begins to sink.


<img src="./docs/incorrect-guess.png" width="700"> 

<br>

If a word with the same number of letters as the target word is suggested, it is checked against the secret word. If the word is a match, the game concludes with a user victory. If not, the user loses a life and the ship descends deeper into the ocean. 

<img src="./docs/word-guess-validation.png" width="700">

<br>

After the first attempt, the letters and words that have already been used are displayed, offering assistance to the user.

The user then continues to guess one letter at a time or opts to propose the entire word until either the correct word is guessed, leading to the game's conclusion, or the user exhausts all lives. 

<img src="./docs/attempted-letters-and-words.png" width="700">

---

### End Game Page
Upon completion of the game, users are transitioned to the End Game Page.

If the word is successfully guessed, the screen showcases a triumphant "Congratulations!" message accompanied by the secret word and ASCII Art to reiterate their success.

<img src="./docs/game-winner.png" width="700">

<br>

In the event of an unsuccessful guess resulting in no lives remaining, the "Good effort!" message appears, followed by the correct word and complemented by an ASCII Art depiction of an ocean without a ship.

<img src="./docs/game-over.png" width="700">

<br>

On this conclusive page, users can either:
  - opt to replay the game, which will redirect them to the Rules Page to choose new lives
  <br>or
  -  conclude the game, redirecting them back to the Welcome Page.

### Future Features to Implement

The game currently lacks personalisation and ownership. I aim to implement a feature enabling users to input their usernames, and their highest (and lowest) scores would be stored in a database, visible to all users through a leaderboard-style interface. This addition, featuring a leaderboard displaying the names and scores of past players, will enhance player engagement and promote continued gameplay.

## Python Libraries Used 
### random:
  - The random library was incorporated to allow the application to randomly select a word from words.py for each game instance.
### os:
  - The os library facilitated communication with the operating system to refresh the terminal at various points throughout the game. This enhanced the user's experience by providing a cleaner and more enjoyable interface.

## Technologies Used
### Programming Language
  - Python was used to build the main content of the game.

### Tools Used To Develop The Game
  - <a href="https://www.gitpod.io/" target="_blank">Gitpod</a> served as the platform for creating, editing, and previewing code throughout the development process.
  - <a href="https://git-scm.com/" target="_blank">Git</a> was employed for version control, managing and tracking changes in the codebase.
  - <a href="https://github.com/" target="_blank">GitHub</a> was utilised to store both the repository and the codes.
  - <a href="https://dashboard.heroku.com/apps" target="_blank">Heroku</a> was chosen as the deployment platform for the application.

### Other Online Resources
  - <a href="https://lucid.app" target="_blank">Lucid Charts</a> was used to plan and create the logical flow of the game.
  - <a href="https://app.grammarly.com/" target="_blank">Grammarly</a> was used to proof all files and remove grammatical and typographical errors.
  - <a href="https://www.notion.so/" target="_blank">Notion</a> was used to make notes and to store essential images throughout the development process. Notion also handled the compression of images in the process.

  ## Testing

### Code Validation

The application underwent thorough validation to identify and rectify any syntax errors. The <a href="https://pep8ci.herokuapp.com/">CI Python Linter</a> was employed for this validation process, and it successfully confirmed the absence of errors in the code.

<details>
  <summary>Validation Results for run.py</summary>
  <img src="./docs/python-linter-run.png" width="700">
</details>

<details>
  <summary>Validation Results for sinking_ship.py</summary>
  <img src="./docs/python-linter-sinking-ship.png" width="700">
</details>

<details>
  <summary>Validation Results for ascii_art.py</summary>
  <img src="./docs/python-linter-ascii-art.png" width="700">
</details>

<details>
  <summary>Validation Results for words.py</summary>
  <img src="./docs/python-linter-words.png" width="700">
</details>

<details>
  <summary>Validation Results for game_over.py</summary>
  <img src="./docs/python-linter-game-over.png" width="700">
</details>

<details>
  <summary>Validation Results for game_winner.py</summary>
  <img src="./docs/python-linter-game-winner.png" width="700">
</details>

<details>
  <summary>Validation Results for font_styles.py</summary>
  <img src="./docs/python-linter-font-styles.png" width="700">
</details>

## Manual Testing


### Welcome Page
| Step  | Description                | Anticipated Outcome                                                        | Observed Outcome                                 | Status      |
| :---: | -------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------ | :---------: |
| 1     | Deployed Website           | Welcome Page loads with no issues                                          | Welcome Page loads as expected                   | Pass        |
| 2     | Display Title ASCII Art    | Title loads with ASCII Art rendering                                       | ASCII Art loads as expected                      | Pass        |
| 3     | Font Styles                | Font styles are displayed correctly                                        | Font styles are displayed as expected            | Pass        |
| 4     | User Input / Clear Terminal| Once the user presses ENTER, the terminal clears and loads the Rules Page  | The terminal clears and the Rules Page is loaded | Pass        |
