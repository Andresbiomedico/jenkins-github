pipeline{
    agent any
    environment {
        IMAGE_NAME = "us-central1-docker.pkg.dev/gtech-324715/jenkins-repo/jenkins"
    }
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
                    sh "gcloud auth list"
                    sh "gcloud projects list"
                    def prNumber = env.CHANGE_ID
                    def imageTag = "pr-${prNumber}"
                    sh "docker push ${IMAGE_NAME}:${imageTag}"
                }

            }
        }
    }
}