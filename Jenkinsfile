pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ganilreddy265/demo-web-application.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo-web-application:latest .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Check if the tests directory exists
                    if (fileExists('tests')) {
                        sh 'pytest tests/'
                   } else {
                        echo "⚠️ No 'tests/' folder found. Running pytest to auto-discover tests."
                        sh 'pytest'
            }
        }
    }
}


        stage('Push Image to Registry') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push Anil9182/demo-web-application:latest'
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
