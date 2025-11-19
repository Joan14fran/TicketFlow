pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
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