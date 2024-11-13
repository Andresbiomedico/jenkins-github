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

                script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker build -t ${IMAGE_NAME}:${imageTag} ."
                }

                 echo 'stage 1 Builds no disponibles'
            }
        }
        stage('Push Docker Image') {
            when {
                    changeRequest()
                }
            steps {

                 echo 'stage 1 Builds no disponibles'
                script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }
            }
        }
    }
}