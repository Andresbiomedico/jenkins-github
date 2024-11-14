pipeline{
    agent any
    environment {
        PROJECT_ID = "gtech-324715"
        CREDENTIALS_ID = "sa-jenkins-pipeline"
        REGION = "us-central1"
        IMAGE_NAME = "${REGION}-docker.pkg.dev/${PROJECT_ID}/jenkins-repo/jenkins"
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
                withCredentials([file(credentialsId: "${CREDENTIALS_ID}", variable: 'GOOGLE_CREDENTIALS_FILE')]) {
                    script {
                        sh 'gcloud auth activate-service-account --key-file=$GOOGLE_CREDENTIALS_FILE'
                        sh "gcloud config set project ${PROJECT_ID}"
                        sh "gcloud auth configure-docker ${REGION}-docker.pkg.dev"

                        def prNumber = env.CHANGE_ID
                        def imageTag = "pr-${prNumber}"
                        sh "docker push ${IMAGE_NAME}:${imageTag}"
                    }
                }
            }
        }
    }
}