pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo Build OK'
                bat 'python build.py'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Test OK'
                bat 'dir dist\\*.html'
            }
        }
    }
}
