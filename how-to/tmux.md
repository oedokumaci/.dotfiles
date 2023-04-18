# Tmux

Terminal multiplexer.

### Check if you have it already
```zsh
which tmux
```
### Install
```zsh
sudo apt-get install tmux
```
or
```zsh
brew install tmux
```

### Important terminology
* session: group of windows, can have a name
* window: basically a tab, can have a name
* pane: part of a window with a shell

### Basic Commands
* Start tmux session: `tmux`
* List tmux sessions: `tmux ls`
* Re-attach tmux session: `tmux a -t <sessionname>`

### Basic Hotkeys inside tmux

##### Session
* Leave tmux while keeping session open (detach): `crtl + b` `d`
* Rename session: `ctrl + b` `$`

##### Window
* Create new window: `crtl + b` `c`
* Rename a window: `ctrl + b` `,`
* Close a window: just `exit` your shell (or do use `ctrl + d`)
* List sessions and windows, allows to switch: `ctrl + b` `w`
* Switch to next window `ctrl + b` `n`
* Switch to previous window `ctrl + b` `p`
* Change window id: `ctrl + b` `.`

* Switch windows TODO

##### Pane
* Split pane vertically `ctrl + b` `"`
* Split pane horizontally `ctrl + b` `%`
* Switch panes `ctrl + b` `arrow key`
* Resize current pane `ctrl + b` `ctrl + arrow key`
* Cycle through pane layouts `ctrl + b` `space`

* Rename session: ...

### Configuration
The configuration `.tmux.conf` lives in your home folder `~`.

My config lives [here](../config.tmux).


Recommended setting: open new panes in same directory
```zsh
bind c new-window -c "#{$HOME}"
bind '"' split-window -c "#{pane_current_path}"
bind % split-window -h -c "#{pane_current_path}"
```


### Recommended plugins
- [Tmux resurrect](https://github.com/tmux-plugins/tmux-resurrect) after system restart your session will be restored

### Installing tmux plugins
To install plugins:

```zsh
# Clone tmux plugin manager
git clone -q https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# Update tmux.conf with the plugins you want (see my tmux.conf for examples)

# This installs the plugins
~/.tmux/plugins/tpm/bin/install_plugins
```