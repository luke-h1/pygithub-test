import os
from github import Github
from dotenv import load_dotenv
import json

g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

def generate_dummy_file():
  if not os.path.exists('test.txt'):
    with open("test.txt","w") as variable_name:
      variable_name.write('test')


def create_pr():
  print('working')
  repo = g.get_repo("luke-h1/pygithub-test")
  body = """ 
  PR from py github
  """
  pr = repo.create_pull(title="testing from py github", body=body, head="develop", base="master")
  print(pr)
  
if __name__ == '__main__':
  load_dotenv()
  generate_dummy_file()
  create_pr()
