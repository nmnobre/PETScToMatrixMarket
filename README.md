# PETSc to Matrix Market

The script operates on the plain text output of `-ksp_view_mat`.
It's been tested on MOOSE's console output, but _should_ work with any application using PETSc as its solver.

### Usage

Given a file `Output.txt` including the output of `-ksp_view_mat`, the converted matrix can be saved in `Matrix.mtx` with:
```
python PETScToMatrixMarket.py Output.txt > Matrix.mtx
```
