pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building the Docker image...'
                    sh '''
                        # Display the Dockerfile (optional, for debugging)
                        cat Dockerfile
                        # Build the Docker image
                        #docker build -t my-docker-image:latest .
                    '''
                }
            }
        }
    }
}
