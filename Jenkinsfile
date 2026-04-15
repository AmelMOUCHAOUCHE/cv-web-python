pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'echo Build OK - fichiers HTML presents'
                bat 'dir'
            }
        }
        stage('Test') {
            steps {
                bat 'echo Test OK - verification des fichiers'
                bat 'dir *.html'
            }
        }
    }
}
