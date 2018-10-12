pipeline {

 agent any
	environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
    stages { 
	     steps {
                git branch: 'pipeline-test',
                credentialsId: 'pipeline-test',//this has been taken from jenkins credentials
                url:"https://github.com/n96perera/jenkins-example/blob/master/testpipe.py"

               sh "ls -lat"
			}	
        }
        stage ('Run Stage') {
            steps {
                withEnv(['PYTHONPATH=C:/Python27']) {
                    bat 'python "https://github.com/n96perera/jenkins-example/blob/master/testpipe.py"'
                }
            }
        }

    }
}
