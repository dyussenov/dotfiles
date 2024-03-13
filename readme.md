# My configurations files

---

## Install Docker

- Get convinience script and install it:

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    ```

    ```bash
    sudo sh get-docker.sh
    ```

- Create docker group and add current user:

    ```bash
    sudo groupadd docker
    ```

    ```bash
    sudo usermod -aG docker $USER
    ```

- Check installation

    ```bash
    docker run hello-world
    ```

## Install Poetry

- Install poetry using the convenience script

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- Add poetry to PATH (.bashrc or .zshrc)

    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```

## Multiple python version using Pyenv

- Istall dependecies (ubuntu example):
    ```bash
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
    ```

- Install using [pyenv-installer](https://github.com/pyenv/pyenv-installer):
    ```bash
    curl https://pyenv.run | bash
    ```

- Add following lines to `~/.bashrc` or whatever:
    ```
    export PATH="$HOME/.local/bin:$PATH"
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    if command -v pyenv 1>/dev/null 2>&1; then
	    eval "$(pyenv init -)"
    fi
    ```

- Install some python versions:
    ```bash
    pyenv isntall 3.9
    pyenv install 3.11
    ```

- Show installed versions:
    ```bash
    pyenv versions
    ```

- Choose version from list:
    ```bash
    pyenv global 3.9
    ```

## Install Alacritty

## Install zsh and oh my zsh

- Install zsh using package manager (don't forget to check installation `zsh --version`):

    ```bash
    pacman -S zsh
    ```

- Set it as default shell and log out:

    ```bash
    chsh -s $(which zsh)
    ```

- Install oh my zsh:

    ```bash
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

- Configure theme adding to `~/.zshrc` following line:

    ```
    THEME=crcandy
    ```


## Touchpad

- libinput

- libinput-gestures https://github.com/bulletmark/libinput-gestures
