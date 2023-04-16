import subprocess

# Install Apple's Command Line Tools, which are prerequisites for Git and Homebrew.
subprocess.run(["xcode-select", "--install"], check=False)

# Clone repo into new hidden directory.
subprocess.run(["git", "clone", "https://github.com/oedokumaci/.dotfiles", "~/Projects/.dotfiles"])

# Create symlinks in the Home directory to the real files in the repo.
subprocess.run(["ln", "-s", "~/Projects/.dotfiles/.zshrc", "~/.zshrc"], check=False)
subprocess.run(["ln", "-s", "~/Projects/.dotfiles/.gitconfig", "~/.gitconfig"], check=False)

# Install Homebrew, followed by the software listed in the Brewfile.
subprocess.run(["/bin/bash", "-c", "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"], check=False)

# Then pass in the Brewfile location...
subprocess.run(["brew", "bundle", "--file", "~/Projects/.dotfiles/Brewfile"], check=False)