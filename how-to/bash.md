### Misc

du -ahx . | sort -rh | head -30

find -iname "*.ipynb" -exec grep -l "20240101" {} \+

---

### Show available aliases, builtins, keywords, functions

```zsh
# will list all the aliases you could run.
compgen -a

# will list all the built-ins you could run.
compgen -b

# will list all the keywords you could run.
compgen -k

# will list all the functions you could run.
compgen -A function

# will list all the above in one go.
compgen -A function -abck
```

---

### Check if word is an aliases, builtin, keyword or function

```zsh
function myfunction() {
    true
}
alias myalias='true'

# examples
type myalias
type if # keyword
type myfunction
type cd # builtin
type nonexistent
```

---

### Open all files matching some regex in VS Code

```zsh
code -r $(git grep -l 'property\.name')
```

---

### Open all files with mypy errors in VS Code

```zsh
code --goto $(pre-commit run mypy -a 2>&1 | cut -d ':' -f 1-2 | grep '\.py')
```

### Update Latex packages

```zsh
sudo tlmgr update --self && sudo tlmgr update --all
```
