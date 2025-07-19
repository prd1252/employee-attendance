pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee-attendance-app'
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                git credentialsId: 'my-git-credentials', url: 'https://github.com/prd1252/employee-attendance.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose down || exit 0'
                bat 'docker-compose up -d'
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
