pipeline {
    agent any

    stages {
        stage('Build App') {
            steps {
                git ('https://github.com/mohamud14/flask-dockerized-jenkins.git')
                echo 'Build'
            }
        }
        stage('Test Web App') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "sudo docker build -t main.py ."
                echo 'Building..'
            }
        }
        stage('Deploy Image') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Deploy to Swarm') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Clean Up') {
            steps {
                echo 'Cleaning....'
            }
        }
    }
}