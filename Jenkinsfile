pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest test_program.py --junitxml=test-reports/result.xml'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}