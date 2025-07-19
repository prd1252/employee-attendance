pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee-attendance-tracker'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/prd1252/employee-attendance-tracker.git'
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
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment successful!'
        }
        failure {
            echo '❌ Build or deployment failed!'
        }
    }
}