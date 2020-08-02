pipeline {
  agent { dockerfile true  }
  stages {
    stage('test') {
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