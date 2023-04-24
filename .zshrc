# Set environment variables
source $HOME/.env

# Set ZSH theme
ZSH_THEME="robbyrussell"

# Set ZSH plugins
plugins=(git)  # MacOS python3 zsh-autosuggestions zsh-syntax-highlighting

# Source oh-my-zsh
source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
source $HOME/.aliases

if [ -n "$PYTHONPATH" ]; then
    export PYTHONPATH=$(which python$PYTHON_VER)'/site-packages/pdm/pep582':$PYTHONPATH
else
    export PYTHONPATH=$(which python$PYTHON_VER)'/site-packages/pdm/pep582'
fi
