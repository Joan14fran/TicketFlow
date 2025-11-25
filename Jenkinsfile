pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'ticketflow'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build & Start') {
            steps {
                script {
                    echo '--- Construyendo y Desplegando Contenedores ---'
                    // CORRECCIÓN AQUÍ: Especificamos los servicios
                    sh 'docker-compose up -d --build backend frontend'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo '--- Verificando Contenedores Activos ---'
                    sh 'docker ps'
                    sleep 10
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Despliegue Exitoso.'
        }
        failure {
            echo 'El despliegue falló.'
        }
    }
}