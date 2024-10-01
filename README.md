# Running a Local Copy of the Data8 Textbook - SeriousCoffeeCup
This repo is for running the Data 8 textbook locally, so you could tweak the code that is being ran to understand it better.

The individual chapters are extracted from the layers of folders onto a single layer, for much easier search of the proper chapter.
If you want to format a fresher copy of the textbook, just take the .py files in the PostProcessingFormattingCode and toss it into an updated repo. If you're not sure what the issue is, you could clone the original repo https://github.com/data-8/textbook and see if you've issues running that.

If nothing else,
go to textbook_chapters\chapters_main and start running the code.

The prerequisites for running this repo is 
- cloning this repo by running git clone [repo name] on your local folder (https://www.atlassian.com/git/tutorials/setting-up-a-repository#:~:text=git%C2%A0clone%C2%A0%3Crepo%C2%A0url%3E).
- Then, using conda (https://docs.conda.io/projects/conda/en/23.3.x/user-guide/install/download.html), open the folder CondaEnvironmentBuild and type conda env create -f PyData.yaml.
- Select PyData as your Python interpreter and run the chapters using it.

See different instructions at:
https://github.com/data-8/zero-to-data-8

Documentation of the datascience library:
https://www.data8.org/datascience/

# Computational and Inferential Thinking

This repository holds the Jupyter Book source for Computational and Inferential
Thinking: The Foundations of Data Science.

## To make a change to the book and update `inferentialthinking.com`

1. Get your copy of this repository:

   ```
   git clone https://github.com/data-8/textbook
   ```
2. Change the file you wish and commit it to the repository.
3. Push your change back to the `data-8/textbook` repository (ideally via a pull request).
4. That's it a GitHub Action will build the book and deploy it to [inferentialthinking.com](https://inferentialthinking.com)


## How this repository is deployed to `inferentialthinking.com`

* The textbook at `inferentialthinking.com` is actually being served from this repository:

  https://github.com/inferentialthinking/inferentialthinking.github.io

  **You should not ever directly edit the inferentialthinking.github.io repository**
* When you make a change to this repository and push it to the `data-8/textbook` `main`
  branch, the book's HTML will automatically be pushed to https://github.com/inferentialthinking/inferentialthinking.github.io.
* This process is handled by [this GitHub Action](.github/workflows/deploy.yml)

## Build and preview the text locally

To build locally, `pip install -r requirements.txt` and then `jupyter-book build .`

**Follow the build instructions on the Jupyter Book guide**. The guide has
information for how to use the Jupyter Book CLI to build this book. You can find
the [Jupyter Book build instructions here](https://jupyterbook.org/start/build.html).
