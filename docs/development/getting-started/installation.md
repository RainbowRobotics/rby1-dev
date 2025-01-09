---
title: Installation  
outline: deep
---

# Installation

This document guides you through the hardware and software preparation steps required to start using the Rainbow Robotics SDK. Follow the instructions based on your development environment, whether you are using C++ or Python.

## 🛠 Requirements

### For C++ Users:
- **Supported OS**: Ubuntu 22.04
- **C++ Compiler**: GCC >= 11
- **Build Tool**: CMake >= 3.30
- **C++ Package Manager**: Conan
- **Other Tools**: Git

### For Python Users:
- **Supported OS**: Ubuntu 22.04
- **Python**: >= 3.10
- **Python Package Manager**: pip

---

## 💻 For C++ Users

### Installing CMake

Check and install the required version of CMake:

```bash
# Check the currently installed CMake version
cmake --version

# If the CMake version is below 3.30, remove the existing version
sudo apt remove --purge cmake
sudo apt autoremove

# Install the latest version
sudo snap install cmake --classic

# Verify the installed version of CMake
cmake --version
```

### Installing Conan

```bash
# Install Conan
pip install conan

# Detect Conan profiles
conan profile detect --force
```

### Installing the SDK

To install and build the Rainbow Robotics SDK for C++ users, follow these steps:

#### Option 1: Clone via SSH (for users with an SSH key)

```bash
git clone --recurse-submodules git@github.com:RainbowRobotics/rby1-sdk.git
```

#### Option 2: Clone via HTTPS

```bash
git clone --recurse-submodules https://github.com/RainbowRobotics/rby1-sdk.git
```

### C++ Usage

```bash
# Install dependency packages
cd rby1-sdk
conan install . -s build_type=Release -b missing -of build

# Create CMake presets
cmake --preset conan-release -D BUILD_EXAMPLES=ON

# Perform the build
cmake --build --preset conan-release
```

## 🐍 For Python Users

Python users can now easily install the SDK via `pip`, as it has been officially released on PyPI.

### Install via `pip`

```bash
pip install rby1-sdk
```

> :warning: **Notice**: If you started using the SDK before October 2024, you might have been using **Poetry** to manage dependencies and the environment. However, the SDK has now been officially released on PyPI, and you can simply install it using `pip`. As a result, the instructions related to Poetry have been removed.

## 🎯 Running Example Programs

Once you have installed the SDK, you can run the example programs for both C++ and Python environments.

> :warning: **IMPORTANT WARNING**: Ensure the surroundings are safe before executing any motion-related programs.

### For C++ Users:

```bash
# Run the C++ example program
./build/examples/cpp/example_demo_motion [RPC IP]:50051
```

### For Python Users:

Ensure the `ROBOT_ADDRESS` is correctly set in `demo_motion.py` before running.

```bash
# Run the Python example program
python examples/python/demo_motion.py 
```
