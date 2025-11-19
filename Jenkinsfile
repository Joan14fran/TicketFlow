pipeline {
    agent any
    
    environment {
        COMPOSE_PROJECT_NAME = 'ticketflow'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Stop Old Containers') {
            steps {
                sh 'docker stop ticketflow_backend ticketflow_frontend || true'
                sh 'docker rm ticketflow_backend ticketflow_frontend || true'
            }
        }
        
        stage('Build Backend') {
            steps {
                sh 'docker-compose build backend'
            }
        }
        
        stage('Build Frontend') {
            steps {
                sh 'docker-compose build frontend'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d backend frontend'
            }
        }
    }
}