pipeline{
    agent any
    environment {
        IMAGE_NAME = "gcr.io/gtech-324715/jenkins"
    }
    stages {
        stage('Build Docker Image') {
            when {
                    changeRequest()
                }
            steps {
                 echo 'stage 1 Builds no disponibles'
            }
        }
        stage('Push Docker Image') {
            when {
                    changeRequest()
                }
            steps {

                 echo 'stage 1 Builds no disponibles'

            }
        }
    }
}