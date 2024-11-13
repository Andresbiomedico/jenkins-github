pipeline{
    agent any
    environment {
        IMAGE_NAME = "gcr.io/gtech-324715/jenkins"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                when {
                    changeRequest()
                }
                script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker build -t ${IMAGE_NAME}:${imageTag} ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                 when {
                    changeRequest()
                }
                script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }
            }
        }
    }
}