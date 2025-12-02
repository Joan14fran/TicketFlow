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

        stage('Build, Test & Coverage') {
            steps {
                script {
                    echo '--- 1. Construyendo Imagen del Backend ---'
                    sh 'docker-compose build backend'
                    
                    echo '--- 2. Ejecutando Tests y Subiendo a Codecov ---'
                    sh """
                        docker-compose run --rm backend sh -c "
                            apt-get update && apt-get install -y curl &&
                            coverage run manage.py test &&
                            coverage xml &&
                            curl -Os https://uploader.codecov.io/latest/linux/codecov &&
                            chmod +x codecov &&
                            ./codecov -t ${CODECOV_TOKEN} -f coverage.xml -C ${env.GIT_COMMIT} -r Joan14fran/TicketFlow -B ${env.BRANCH_NAME}
                        "
                    """
                }
            }
        }

        stage('Deploy (Start App)') {
            steps {
                script {
                    echo '--- 3. Despliegue Final ---'
                    sh 'docker-compose up -d backend frontend'
                }
            }
        }
        
        stage('Verify') {
            steps {
                script {
                    echo '--- Verificando estado ---'
                    sh 'docker ps'
                }
            }
        }
    }
    
    post {
        always { echo 'Pipeline finalizado.' }
        success { echo '¡Éxito total! Tests pasados y código desplegado.' }
        failure { echo 'Fallaron las pruebas. Revisa los logs.' }
    }
}