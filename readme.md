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

## Install Alacritty

## Install zsh and oh my zah

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
