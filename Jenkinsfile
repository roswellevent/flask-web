pipeline
{
  environment {
    registry = "roswellevent/flask-web-images"
    registryCredential = "DockerHub"
  }
  agent none
  stages
  {

          stage('Test') {
            agent { dockerfile true }
             steps {
                echo 'Testing Now'
                  withEnv(["HOME=${env.WORKSPACE}"]) {
                      sh 'pytest test_program.py --junitxml=test-reports/result.xml'
                      junit 'test-reports/*.xml'
                  }
              }
          }


       stage('Build') {
             agent any
             steps {
                echo 'Building Container from Dockerfile'
             //   sh 'docker build -t jenkins-demo:${BUILD_NUMBER} . '
                 script {
                     customImage = docker.build("${env.registry}:${env.BUILD_ID}")
                 //   customImage.push()
                 }
             }
       }

      stage('Deploy Image!') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            customImage.push("${env.BUILD_ID}")
            customImage.push("latest")
           // sh "docker push my-docker-image:${env.BUILD_ID}"
          }
        }
      }
    }



  }
}