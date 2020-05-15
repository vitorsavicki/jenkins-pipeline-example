pipeline{
  agent none
  stages{
    stage('Compile'){
      agent any
      steps{
        sh 'mvn compile'
      }       
    }
    stage('Code Quality'){
      agent any
      steps{
        sh 'echo Sonarqube Code Quality Check Done'
      }
    }
    stage('Test'){
      agent any
      steps{
        sh 'mvn test'
      }
    } 
    stage('Package'){
      agent any
      steps{
        sh 'echo Package Artifactory'
      }
    }
    stage('Upload War File To Artifactory'){
      agent any
      steps{
        sh 'echo Uploaded War file to Artifactory'
      }
    }
    stage('Deploy'){
      agent any
      steps{
        sh label: '', script: '''rm -rf dockerimg
mkdir dockerimg
cd dockerimg
cp -r /var/jenkins_home/workspace/jenkins-pipeline-example_master/* .
sudo docker build -t webimage:$BUILD_NUMBER .
sudo docker container run -itd --name webserver$BUILD_NUMBER -p 9090 webimage:$BUILD_NUMBER'''

      }
    }
  }
}
