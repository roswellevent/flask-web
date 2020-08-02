pipeline {
  agent none
  stages {
    stage('Build') {
         agent { dockerfile true  }
         steps {
            echo 'Building Conatiner from Dockerfile'
         }
    }
    stage('Test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'pytest test_program.py --junitxml=test-reports/result.xml'
        }
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}