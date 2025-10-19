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

//         stage('Run Unit Tests') {
//             steps {
//                 script {
//                     // Check if the tests directory exists
//                     if (fileExists('tests')) {
//                         pip install -r requirements.txt
//                         sh 'pytest tests/'
//                    } else {
//                         echo "⚠️ No 'tests/' folder found. Running pytest to auto-discover tests."
//                         sh 'pytest'
//             }
//         }
//     }
// }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm demo-web-application:latest pytest -v'
    }
}

        stage('Push Image to Registry') {
            steps {
                withDockerRegistry([ credentialsId: 'dockerhub-credentials', url: '' ]) {
                    sh 'docker tag demo-web-application:latest anil9182/demo-web-application:latest'
                    sh 'docker push anil9182/demo-web-application:latest'
        }
    }
}


        stage('Deploy with Ansible') {
            steps {
                sh "ansible-playbook ansible/site.yml -i ansible/inventory -e target_env=${params.TARGET_ENV}"
        }
    }

    }

    post {
        failure {
            echo 'Deployment failed.'
        }
    }
}
