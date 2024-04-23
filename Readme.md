# Platform.sh Django3 project integration with GitHub account
1. Create GitHub repo
2. create GitHub [token](https://docs.platform.sh/integrations/source/github.html)
3. login to platform.sh, install platform.sh [CLI](https://docs.platform.sh/administration/cli.html)
4. create platform.sh project (`platform create --title test-django-project`) OR add git repo to existing project - `platform project:set-remote <PROJECT_ID>`
5. Add GitHub [integration](https://docs.platform.sh/integrations/source/github.html):
```
platform integration:add \
  --project <PROJECT_ID> \
  --type github \
  --repository <USERNAME>/<REPO> \
  --token <GITHUB_TOKEN>
```

6. add Platform.sh  configuration files
    mkdir -p .platform && touch .platform/services.yaml && touch .platform/routes.yaml && touch .platform.app.yaml

7. Config example [here](https://github.com/platformsh-templates/django3).

8. Now your app is connected to GitHub, by default every push will trigger a new build in platform.sh

7. Connect to your env - [instruction](https://docs.platform.sh/development/ssh.html)  
  `# create admin user`  
  `python manage.py createsuperuser`
