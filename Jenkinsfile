pipeline {
  agent none
  stages {
        stage('Build & Test') {
            agent { dockerfile true }
             steps {
                echo 'Building Conatiner from Dockerfile'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'pytest test_program.py --junitxml=test-reports/result.xml'
              }
          }

        }

          post
          {
            always {
              junit 'test-reports/*.xml'
            }
            success {
                        echo "======Build OK!!!!======="

            }
          }
    }
  }