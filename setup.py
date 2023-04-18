import subprocess
from pathlib import Path

DOT_FILES = [".zshrc", ".gitconfig", ".tmux.conf"]

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
            src_file: Path = Path.home() / dot_file
            dst_file: Path = Path.home() / ".dotfiles" / dot_file
            subprocess.run(["mv", str(src_file), str(dst_file)], check=False)

            # create symlink in the home directory to the real file in the repo
            subprocess.run(["ln", "-s", str(dst_file), str(src_file)], check=False)
