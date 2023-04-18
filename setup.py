import subprocess
import os

DOT_FILES = [".zshrc", ".gitconfig"]

if __name__ == "__main__":
    if (input("Install homebrew and the software in the brewfile? (Y/n): ") or "y") == "y":
        # install homebrew
        subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"], check=False)

        # install software in the brewfile
        subprocess.run(["brew", "bundle", "--file", "~/.dotfiles/Brewfile"], check=False)

    for dot_file in DOT_FILES:
        if (input(f"Install {dot_file}? (Y/n): ") or "y") == "y":            
            # move the dotfile to .dotfiles
            src_file = os.path.expanduser(f"~/{dot_file}")
            dst_file = os.path.expanduser(f"~/.dotfiles/{dot_file}")
            subprocess.run(["mv", src_file, dst_file], check=False)

            # create symlink in the home directory to the real file in the repo
            subprocess.run(["ln", "-s", dst_file, src_file], check=False)
