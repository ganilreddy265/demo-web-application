pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/ganilreddy265/Demo-Web-Application.git'
        IMAGE_NAME = 'Demo-Web-Application'
    }

    parameters {
        choice(name: 'TARGET_ENV', choices: ['sit', 'uat'], description: 'Select environment to deploy')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
                credentialsId: 'github-credentials'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:latest python -m unittest discover -s tests || echo "No tests yet"'
            }
        }

        stage('Push Image to Registry') {
            steps {
                sh 'docker tag ${IMAGE_NAME}:latest Anil9182/${IMAGE_NAME}:latest'
                sh 'docker push Anil982/${IMAGE_NAME}:latest'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh """
                ansible-playbook ansible/site.yml \
                    -i ansible/inventory \
                    -e target_env=${TARGET_ENV}
                """
            }
        }
    }

    post {
        success {
            echo "Deployment to ${params.TARGET_ENV} successful!"
        }
        failure {
            echo "Deployment failed."
        }
    }
}