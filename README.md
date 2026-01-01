# uni

A personal cli tool to install packages across different linux distributions

## Warning :warning:
This project is a work in progress (WIP).

This project exists to support my personal workflows and learning goals. Design decisions, features and defaults are intentionally optimized for these use cases and not for general adoption.

At this stage:
- APIs, configuration formats and behavior may change without notice
- Backward compatibility is **not** guaranteed
- Documentation may be incomplete or outdated
- The project is **not** intended for mass usage or production environments

Stability, extensibility and broader usability may be considered in the future, but they are **not goals right now**.

## Testing
```bash
# testing in ubuntu
docker run -it --rm -v $(pwd):/uni ubuntu:22.04 bash

apt update && apt install -y python3 ca-certificates
cd /uni
python3 -m uni.main nvim
```

```bash
# testing in almalinux
docker run -it --rm -v $(pwd):/uni almalinux:9.7 bash

cd /uni
python3 -m uni.main nvim
```

```bash
# testing in archlinux
docker run -it --rm -v $(pwd):/uni archlinux/archlinux bash

yes | sudo pacman -Sy python
cd /uni
python3 -m uni.main nvim
```
