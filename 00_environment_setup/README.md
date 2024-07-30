# Environment setup

This readme describes the steps of configuring your environment for the *python-advanced* course.

1. Download and install [winpython](https://github.com/winpython/winpython/releases/download/8.2.20240618final/Winpython64-3.12.4.1dot.exe).
2. Extract to user directory.
3. Install [VSCode](https://code.visualstudio.com/docs/python/python-tutorial).
4. Clone this repository `git clone https://github.com/Artillence/python-advanced.git` or download the latest version using [this link](https://github.com/Artillence/python-advanced/archive/refs/heads/main.zip).

2. **Create a Virtual Environment (`venv`)**:
    - Open `C:\Users\Administrator\Desktop\WPy64-31241\WinPython Command Prompt.exe` and navigate to your working directory:
      ```sh
      cd C:\Users\Administrator\python-advanced
	  
	  # Create venv
      C:\Users\Administrator\Desktop\WPy64-31241\python-3.12.4.amd64\python.exe -m venv venv
	  
	  venv\Scripts\activate
	  pip install jupyterlab
      ```

5. **Start JupyterLab**:
    - While still in the virtual environment, start JupyterLab:
      ```sh
      jupyter-lab
      ```
    - JupyterLab will open in your default web browser. You can now create and manage your Jupyter notebooks in the specified working directory.
