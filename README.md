# myword
A word game similar to the NYT Wordle

You will guess a secret, 6 letter, word over 11 rounds.
Each round you will guess a smaller word of 2 to 5 letters.
The first word will correspond to the first two positions of the secret word.
The second word will correspond to the first three positions of the secret word.
After that the positions will start to shift, as you can see in the graphic below.
For every word you guess, if it has a letter that matches with the secret word you will get 1000 points if they are in the same spot and 250 if they are in different spots.

```_ _ - - - -   Round 1
_ _ _ - - -   Round 2
- _ _ _ - -   Round 3
- - _ _ _ -   Round 4
- - - _ _ _   Round 5
- - _ _ _ _   Round 6
- _ _ _ _ -   Round 7
_ _ _ _ - -   Round 8
_ _ _ _ _ -   Round 9
- _ _ _ _ _   Round 10
_ _ _ _ _ _   Round 11
```

Each of you guesses must be a word in the dictionary (defined as the words in the various json files attached).
On round 11 you have a chance to guess the entire secret word, and if you get it right you get a bonus 3000 points.
This game was originally meant to be played against another human who also is trying to guess a word that you came up with, hence the point structure. Feel free to compete with your friends. Perhaps set a timer and take turns, seeing who can get the highest score.

If the secret word was "JINXED", and your first guess was "HI" you would get 1000 points because you have an I in the second position. If your fourth guess was "HIM" you would get 250 points for having an I, however round 4 is for guessing positions 3, 4, and 5, so your I is in position 4 of the secret word and therefore doesn't line up correctly for the 1000 points.