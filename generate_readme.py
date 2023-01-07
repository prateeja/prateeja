from github import Github
from googletrans import Translator


class GitHubParser:
    def __init__(self):
        self.github_client = Github(${{ secrets.README_GENERATOR_API_KEY }})
        self.translator = Translator()

    def get_starred_repos(self):
        return [repo for repo in self.github_client.get_user().get_starred()]

    def get_stargazers_count(self, repo):
        return repo.stargazers_count

    def generate_readme_text(self):
        repos = self.get_starred_repos()

        f = open('README.md', 'w+')
        f.write("# Starred Repositories\n\n")
        f.write("A list of awesome repositories I've starred. Total starred repositories: `" + str(len(repos)) + "`\n\n")
        f.write("## Contents\n\n")

        repos.sort(key=self.get_stargazers_count, reverse=True)

        for repo in repos:
            full_name = repo.full_name
            description = repo.description
            description = self.translator.translate(repo.description).text if repo.description else ''
            topics = repo.topics
            url = repo.html_url
            stars_url = "https://img.shields.io/github/stars/" + full_name + "?style=social"
            forks_url = "https://img.shields.io/github/forks/" + full_name + "?style=social"

            topic_tags = ["`#" + topic + "`" for topic in topics if topics]

            text = "1. [" + str(full_name) + "](" + str(url) + ")  ![GitHub Repo stars](" + stars_url + \
                   ")  ![GitHub Repo forks](" + forks_url + ")<br/>" + str(description) + "<br/>" + " ".join(topic_tags)
            f.write(text + "\n\n")
        f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = GitHubParser()
    parser.generate_readme_text()

