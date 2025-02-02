# ProjectBuilder
Utility designed to make building and resolving dependencies for OesusDevelopmentStudios projects. Mainly designed to make development and testing easier.

## Supported projects
* [AiMusicBot](https://github.com/OesusDevelopmentStudios/AiMusicBot)
* [~~Prolog~~](https://github.com/OesusDevelopmentStudios/proLog)

## Setup
1. Clone this repository into your home directory. (Or any other place you want)
2. Create virtaul env in the script directory by calling:

```
python3 -m venv .venv
```

3. Install requirements.txt

```
 pip3 install -r requirements.txt
```

4. Add the following lines to your shell config (~/.bashrc, ~/.zshrc):
```
export PATH=$PATH:/home/$USER/ProjectBuilder
alias project_builder="project_builder.py"
```

The following config will allow you to execute the above script from anywhere
