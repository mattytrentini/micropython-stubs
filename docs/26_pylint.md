 # Pylint: Configure pylint to use the selected stub folders
This instructs pylint to insert the list of paths into `sys.path` before performing linting, thus allowing it to find the stubs and use them to better validate your code. 

- use the {download}`.pylintcr sample file <samples/.pylintrc>`.

- edit the line that starts with `init-hook=`  
        ``` ini
        init-hook='import sys;sys.path[1:1] = ["src/lib", "folder1","folder2", "folder3",];'
        ```
- replace the folders with your selection of stub folders.
**Note that in `.pylintrc` In this case they MUST be on a single line**
- the result should look like:
        ``` ini
        init-hook='import sys;sys.path[1:1] = ["src/lib", "all-stubs/cpython_patch","all-stubs/mpy_1_13-nightly_frozen/esp32/GENERIC", "all-stubs/esp32_1_13_0-103",];'
        ```