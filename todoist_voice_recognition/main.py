import os

from todoist_api_python.api import TodoistAPI

my_token = os.getenv("TODOIST_TOKEN")
api = TodoistAPI(my_token)


def main():
    try:
        projects = api.get_projects()
        print(projects)

    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
