# A-CRUD-APP

diagram, video and documentation: 

This is my simple CRUD app which allows you to create a football team and add players
to the team.For one team there are many players. It fulfils the brief by allowing 
create, read, update and delete functionality.

The app is built using the Flask framework. The automated server used is Jenkins and I created
a pipeline which runs gets app, unit tests, builds the docker image, pushes the image to 
a registry and finally deploys to swarm. There is also a GitHub Webhook, so whenever there is
a chane to my GitHub repository the pipeline is triggered. The Docker swarm has one manager 
and one worker. 

Futue improvements can include error handling, more unit tests (maybe implementing selenium),
better user interface and verifying correct team names.
