import subprocess
from pathlib import Path

DOT_FILES = [".aliases", ".env", ".gitconfig", ".tmux.conf", ".vimrc", ".zshrc"]

if __name__ == "__main__":
    if (input("Install homebrew and the software in the brewfile? (Y/n): ") or "y") == "y":
        # install homebrew
        subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"], check=False)

    if (input("Install oh-my-zsh? (Y/n): ") or "y") == "y":
        # install oh-my-zsh
        subprocess.run(["sh", "-c", "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"], check=False)

    if (input("Install the software in the brewfile? (Y/n): ") or "y") == "y":
        # install software in the brewfile
        subprocess.run(["brew", "bundle", "--file", str(Path.home() / ".dotfiles" / "Brewfile")], check=False)

    for dot_file in DOT_FILES:
        if (input(f"Install {dot_file}? (Y/n): ") or "y") == "y":
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

    if (input("Your .dotfiles is kept at ~/.dotfiles. Do you want to create a symlink to it? (Y/n): ") or "y") == "y":
        sym_dir = input("Enter the absolute path to the directory you want to create the symlink in: ")
        subprocess.run(["ln", "-s", str(Path.home() / ".dotfiles"), sym_dir], check=False)
