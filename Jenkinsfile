pipeline{
    agent any
    stages {
        stage('Build Docker Image') {
            when { branch 'PR-*' }
            steps {
                 script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker build -t ${IMAGE_NAME}:${imageTag} ."
                }
            }
        }
        stage('Push Docker Image') {
            when { branch 'PR-*' }
            steps {
                 script {
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }

            }
        }
    }
}