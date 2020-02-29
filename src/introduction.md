# Introduction

Step 1. Run:
```
git clone https://github.com/bCom5/mdbook-notes-template.git
```
This downloads the folder.

Step 2. Edit `first_time.sh` for new GitHub repo. Run `sh first_time.sh`

Step 3. Rename directory. Rename title in `book.toml`.

Step 4. Change location in `deploy.sh`.

Step 5. Run `mdbook serve` and have fun!

Great tools!
* [Imgur Screenshot](https://github.com/jomo/imgur-screenshot)

Aliases for this for quick and easy editing:
```sh
alias i='imgur-screenshot.sh -o false; {echo -n '\''\n\n![]('\''; pbpaste; echo -n '\'')\n\n* '\''} | pbcopy'
alias imgur=imgur-screenshot.sh
alias ii="imgur-screenshot.sh -o false; {echo -n '![]('; pbpaste; echo -n ')\n'} | pbcopy"
```
