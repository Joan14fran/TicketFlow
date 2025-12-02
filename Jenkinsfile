pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'ticketflow'
        CODECOV_TOKEN = '2bc00fef-5431-47df-a258-563284d9fa00' 
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests & Coverage') {
            steps {
                script {
                    echo '--- 1. Ejecutando Pruebas Unitarias (Backend) ---'
                    docker.image('python:3.11-slim').inside('-u root') {
                        sh 'pip install -r back_TicketFlow/requirements.txt'
                        dir('back_TicketFlow') {
                            sh 'coverage run manage.py test'
                            sh 'coverage xml'
                        }
                    }
                }
            }
        }
        
        stage('Upload to Codecov') {
            steps {
                script {
                    echo '--- 2. Subiendo reporte a Codecov ---'
                    docker.image('curlimages/curl:latest').inside {
                        sh 'curl -Os https://cli.codecov.io/latest/linux/codecov'
                        sh 'chmod +x codecov'
                        sh './codecov -t $CODECOV_TOKEN -f back_TicketFlow/coverage.xml'
                    }
                }
            }
        }

        stage('Build & Start (Local)') {
            steps {
                script {
                    echo '--- 3. Despliegue Final (Verificación) ---'
                    sh 'docker-compose up -d --build backend frontend'
                }
            }
        }
    }
    
    post {
        always { echo 'Pipeline finalizado.' }
        success { echo '¡Éxito! Pruebas pasadas, reporte subido y despliegue exitoso.' }
        failure { echo 'Fallo crítico. Revisa los errores.' }
    }
}