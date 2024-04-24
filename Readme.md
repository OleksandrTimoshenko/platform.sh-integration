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

6. Check Platform.sh  configuration files:
- .platform/services.yaml
- .platform/routes.yaml
- .platform.app.yaml

7. Config example [here](https://github.com/platformsh-templates/django3).

8. Create ENV variable for Django secret:
`platform variable:create --level project --name DJANGO_SECRET_KEY --value 'YOUR_APP_KEY_HERE' --visible-build true --visible-runtime true`

9. Now your app is connected to GitHub, by default every push will trigger a new build in platform.sh

10. Connect to your env - [instruction](https://docs.platform.sh/development/ssh.html)  
  `# create admin user`  
  `python manage.py createsuperuser`