# Introduction

Step 1. Run:
```
git clone https://github.com/bCom5/mdbook-notes-template.git
```
This downloads the folder.

Step 2. Change the folder name

Step 3. Run `python first_time.py`

Step 4. Use `mdbook serve` have fun!

Step 5. When want to deploy, cancel out of `mdbook serve`, and run `python deploy.py`

Great tools!
* [Imgur Screenshot](https://github.com/jomo/imgur-screenshot)

Aliases for this for quick and easy editing:
```sh
alias i='imgur-screenshot.sh -o false; {echo -n '\''\n\n![]('\''; pbpaste; echo -n '\'')\n\n* '\''} | pbcopy'
alias imgur=imgur-screenshot.sh
alias ii="imgur-screenshot.sh -o false; {echo -n '![]('; pbpaste; echo -n ')\n'} | pbcopy"
```

