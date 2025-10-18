pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ganilreddy265/Demo-Web-Application.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo-web-application:latest .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Push Image to Registry') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push yourdockerhubusername/demo-web-application:latest'
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        failure {
            echo 'Deployment failed.'
        }
    }
}
