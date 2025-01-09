pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from SCM...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project.....'
                cat Dockerfile
            }
        }
    }
}
