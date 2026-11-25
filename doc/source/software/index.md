# Software & SDK

How the robot software works and how to control the robot with the SDK. For class-by-class details, see the [API Reference](../sdk/index.rst).

`````{grid} 1 2 2 3
:gutter: 3

````{grid-item-card} Software Architecture
:link: architecture
:link-type: doc

Robot PC, user PC and how they communicate.
````

````{grid-item-card} Robot Main Program
:link: robot_main_program
:link-type: doc

Control Manager states and the main program.
````

````{grid-item-card} Robot Models
:link: ../sdk/models/index
:link-type: doc

Model A, M and UB: joints, indexes and versions.
````

````{grid-item-card} Controllers
:link: ../sdk/controllers/index
:link-type: doc

Command architecture, hold time and parameters.
````

````{grid-item-card} Examples
:link: ../examples/ex
:link-type: doc

C++ and Python example programs.
````

````{grid-item-card} Troubleshooting
:link: ../sdk/trobuleshooting/index
:link-type: doc

Build issues, error reporting and FAQ.
````
`````

```{toctree}
:hidden:
:maxdepth: 2

architecture
robot_main_program
../sdk/models/index
../sdk/controllers/index
../examples/ex
../sdk/trobuleshooting/index
```
