# ServerCloner
This project was made to allow users to copy servers without having the `Administrator` permission when they're unable to add a bot to the server.

## Setup
- Download as a ZIP, or `git clone https://github.com/ElijahGives/ServerCloner.git`
- Run `install.bat`
- Run `start.bat`. If it doesn't work, edit it with your python prefix, it's default set to `py`.

## Known Bugs
- Channel overwrites not being copied. The reason for this is because it's getting overwrites from other guild which means when it updates the overwrites, it tries to add overwrites from the old server which wouldn't work because you cant add permission overwrites from roles that aren't in the same server. I'm stumped on a fix, if anyone wants to make a PR with one, go ahead.
- Going from creating channels to creating roles is randomly slow, probably due to ratelimits.

## License
Copyright (c) 2021 ElijahGives.