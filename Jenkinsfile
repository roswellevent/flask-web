pipeline
{
  agent any
  stages
  {

       stage('Build') {
             steps {
                echo 'Building Container from Dockerfile'
                 script {
                    def customImage = docker.build("my-image:${env.BUILD_ID}")
                    customImage.push()
                }
          }


  }

 }