## Steps to bootstrap a new Mac

0. Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.

```zsh
xcode-select --install
```


1. Clone repo into new hidden directory.

```zsh
git clone https://github.com/oedokumaci/.dotfiles ~/.dotfiles
```


2. You can run the setup script for steps 3 and 4 below or do them manually.

```zsh
python setup.py
```

3. Install Homebrew, followed by the software listed in the Brewfile.

```zsh

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then pass in the Brewfile location...
brew bundle --file ~/.dotfiles/Brewfile

# ...or move to the directory first.
cd ~/.dotfiles && brew bundle
```


4. Create symlinks in the Home directory to the real files in the repo for each dotfile.

```zsh
ln -s ~/.dotfiles/.some_dotfile ~/.some_dotfile
```


## Notes
- If you would like to keep your .dotfiles folder in a different location, you can use the setup script as is and later create a symlink to the .dotfiles folder in your home directory.


## To-do

- Learn how to use [`defaults`](https://macos-defaults.com/#%F0%9F%99%8B-what-s-a-defaults-command) to record and restore System Preferences and other macOS configurations.
- Make a checklist of steps to decommission your computer before wiping your hard drive.
- Create a [bootable USB installer for macOS](https://support.apple.com/en-us/HT201372).
- Integrate other cloud services into your Dotfiles process (Dropbox, Google Drive, etc.).


## Credits

### Dotfiles
[Dotfiles from Start to Finish-ish](https://www.udemy.com/course/dotfiles-from-start-to-finish-ish/ "Learn Dotfiles from Start to Finish-ish on Udemy"
)

### How to
https://github.com/lk16/dotfiles/tree/master/howto
