import subprocess
from pathlib import Path

DOT_FILES = [".aliases", ".env", ".gitconfig", ".tmux.conf", ".vimrc", ".zshrc"]

if __name__ == "__main__":
    install_homebrew = input("Install homebrew? (Y/n): ").casefold() or "y"
    if install_homebrew == "y":
        # install homebrew
        subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"], check=False)

    for dot_file in DOT_FILES:
        if (input(f"Install {dot_file}? (Y/n): ").casefold() or "y") == "y":
            # move the dotfile to .dotfiles
            local_dot_file: Path = Path.home() / dot_file
            github_dot_file: Path = Path.home() / ".dotfiles" / dot_file
            try:
                subprocess.run(["mv", str(local_dot_file), str(github_dot_file)], check=True)
                print(f"Moved {local_dot_file} to {github_dot_file}. Check git diff to see the changes.")
            except subprocess.CalledProcessError:
                pass

            # create symlink in the home directory to the real file in the repo
            subprocess.run(["ln", "-s", str(github_dot_file), str(local_dot_file)], check=False)

    if (input("Install oh-my-zsh? (Y/n): ").casefold() or "y") == "y":
        # install oh-my-zsh
        subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"], check=False)

    if (install_homebrew == "y") and (input("Install the software in the brewfile? (Y/n): ").casefold() or "y") == "y":
        # install software in the brewfile
        subprocess.run(["brew", "bundle", "--file", str(Path.home() / ".dotfiles" / "Brewfile")], check=False)

    if (input("Your .dotfiles is kept at ~/.dotfiles. Do you want to create a symlink to it? (Y/n): ").casefold() or "y") == "y":
        sym_dir_input = input("Enter the absolute path to the directory you want to create the symlink in: ")
        sym_dir = Path(sym_dir_input).expanduser()
        sym_dir.mkdir(parents=True, exist_ok=True)

        dotfiles_path = Path.home() / ".dotfiles"
        symlink_target = sym_dir / ".dotfiles"

        # Create symlink
        subprocess.run(["ln", "-s", str(dotfiles_path), str(symlink_target)], check=False)
