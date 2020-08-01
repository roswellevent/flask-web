pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
       withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'echo "***************************************************"'
            sh 'echo $HOME'
            sh 'echo "***************************************************"'
            sh 'pip install --user -r requirements.txt'
      }

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