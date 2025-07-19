pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee-attendance-app'
    }

    options {
        skipDefaultCheckout() // avoids duplicate checkout
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                git credentialsId: 'my-git-credentials', url: 'https://github.com/prd1252/employee-attendance.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    sh 'docker-compose down || true'
                    sh 'docker-compose up -d'
                }
            }
        }
    }

    post {
        failure {
            echo "❌ Build or deployment failed!"
        }
        success {
            echo "✅ Build and deployment completed successfully."
        }
    }
}
