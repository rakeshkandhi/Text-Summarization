import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_desc = f.read()


__version__="0.0.0"

REPO_NAME="End to end Text Summarization Project"
AUTHOR_NAME="rakeshkandhi"
SRC_REPO="Text_Summarization"
AUTHOR_EMAIL="rakeshkandhi1432@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Text summarization project",
    long_description=long_desc,
    long_description_content="text/markdown",
    url="https://github.com/rakeshkandhi/Text-Summarization.git",
    project_urls={
        "Bug Tracker":"https://github.com/rakeshkandhi/Text-Summarization.git/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
