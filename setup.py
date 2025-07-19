import setuptools 

with open("README.md","r",encoding="latin-1") as f:
    long_description=f.read()


__version__ = "1.0.0"

REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="Shakshi123pal"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="Shakshipal591@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url="https://github.com/" + AUTHOR_USER_NAME + "/" + REPO_NAME,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"": "src"},
    package=setuptools.find_packages(where="src")
)

