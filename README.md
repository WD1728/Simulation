# Unified BARN + DynaBARN Gazebo Simulator (Prototype 1)

## 1. Overview
This repository implements a unified simulation environment that combines static BARN layouts with dynamic DynaBARN obstacle trajectories. Each simulation world consists of:
- a static maze (from BARN), and
- moving cylindrical obstacles driven by deterministic motion profiles (from DynaBARN)

This unified environment supports benchmarking for navigation, control, and RL/MPC methods, and will serve as the foundation for Prototype-2, where robotic agents will be introduced into the environment.

## 2. Dataset Characteristics
The DynaBARN generation process outputs three aligned components:

- `N` static worlds
- `N` dynamic worlds
- `N` motion controller plugins

N is defaultly setted as 200. 

Providing only a small subset of dynamic plugins (e.g., `obs_7`, `obs_32`, `obs_180`) is insufficient for full reproducibility.

## 3. Repository Structure
```
Simulation/
├── worlds_static/         # static BARN environments (seed-aligned)
├── worlds_dynamic/        # dynamic DynaBARN environments (XML + plugin references)
├── worlds_unified/        # merged static + dynamic SDF worlds
└── plugins/               # trajectory plugins needed in DynaBARN worlds
    ├── obs_0001.cc
    ├── obs_0002.cc
    ├── ...
    ├── obs_0200.cc
    └── CMakeLists.txt
```

Compiled `.so` shared libraries are not stored to avoid platform dependency and large binary footprints. All plugin source code and build files are portable and compiled locally.

## 4. Dependencies
Gazebo compatibility:
- Ubuntu 20.04: `Gazebo 11` + `libgazebo11-dev`

Build tools:
- `cmake ≥ 3.10`
- `build-essential`

## 5. Plugin Compilation
From:
```
Simulation/plugins/
```

Run:
```
mkdir -p build
cd build
cmake ..
make -j8
```

Produces:
```
libobs_0001.so
libobs_0002.so
...
libobs_0200.so
```

## 6. Unified World Generation
Static and dynamic worlds are matched via seed index:

```
static_seed_XXXX.world
dynamic_seed_XXXX.world
→ unified_seed_XXXX.world
```

Merged output is written to:

```
Simulation/worlds_unified/
```

## 7. Running Unified Worlds
Before launching Gazebo, export plugin path:

```
export GAZEBO_PLUGIN_PATH=$PWD/Simulation/plugins/build:$GAZEBO_PLUGIN_PATH
```

Run a unified scenario:

```
gazebo Simulation/worlds_unified/unified_seed_0001.world
```
