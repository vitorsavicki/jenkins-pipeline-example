pipeline{
  agent none
  stages{
    stage('Compile'){
      agent any
      steps{
        sh 'echo Install Dependencies'
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
        sh 'echo Test Python'
      }
    } 
    stage('Package'){
      agent any
      steps{
        sh 'echo Package Artifactory'
      }
    }
    stage('Upload File To Artifactory'){
      agent any
      steps{
        sh 'echo Uploaded file to Artifactory'
      }
    }
     stage('Build'){
      agent any
      steps{
        sh label: '', script: '''
        sudo docker build -t webimage:$BUILD_NUMBER .'''

      }
    }
    stage('Deploy'){
      agent any
      steps{
        sh label: '', script: '''
        sudo docker container run -itd --name webserver$BUILD_NUMBER -p 4000:4000 webimage:$BUILD_NUMBER'''


      }
      stage('Notify') {

        script { 
        def build = currentBuild // global variable in pipeline -> https://opensource.triology.de/jenkins/pipeline-syntax/globals#currentBuild

        def targetUrl = "https://ancient-moose-15.loca.lt/hubot/jenkins?room=chatops"
        def buildUrl = build.absoluteUrl
        def buildNumber = build.number
        def buildStatus = build.currentResult

        httpRequest url: targetUrl, contentType: 'APPLICATION_JSON', httpMode: 'POST', responseHandle: 'NONE', timeout: 30, requestBody: """
        {
            "name": "${args.serviceName}",
            "build": {
                "full_url": "${buildUrl}",
                "number": "${buildNumber}",
                "phase": "FINISHED",
                "status": "${buildStatus}"
            }
        }
        """
    }
    }
  }
}
