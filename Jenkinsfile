pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
       withEnv(["HOME=${env.WORKSPACE}"]) {
            sh 'echo "***************************************************"'
            sh 'echo $HOME'
             sh 'echo "++++++++++"'
            sh 'echo $PATH'
            sh 'echo "***************************************************"'
            sh '. .env/bin/activate'
            sh 'pip install --user -r requirements.txt'
            sh 'pip install --user -U pytest'
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