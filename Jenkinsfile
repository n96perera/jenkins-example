pipeline {

 agent any
 
    environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
    stages {
        stage ('Run Stage') {
            steps {
                withEnv('PYTHONPATH=C:/Python27') {
                    sh 'python https://github.com/n96perera/jenkins-example/blob/master/testpipe.py'
                }
            }
        }

    }
}
