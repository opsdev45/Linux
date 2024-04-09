pipeline {
  agent any 

  stages {
    stage('Build docker image'){
      steps {
        script{
          docker.build(pipe1)
        }
      }
    }
  stage('Run docker container'){
    steps{
      scripts{
        docker.image(pipe1).run()
        }
      }
    }
  }
}
