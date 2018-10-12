pipeline {

 agent any
	environment {
        JAVA_HOME="${tool 'Java 8u181'}"
        PATH="${JAVA_HOME}/bin:${PATH}"
    }
	
	 parameters {
        booleanParam (
            name: 'git',
            defaultValue: false,
            description: 'Check to run git')
        string(name: 'RELEASE_IDENTIFIER', defaultValue: 'dev-SNAPSHOT', description: '	release.identifier field (Possible values: dev-SNAPSHOT, SNAPSHOT and RELEASE. Default is dev-SNAPSHOT).')
        string(name: 'BRANCH', defaultValue: 'dev', description: 'Git branch to build.')
        string(name: 'gitLocation', defaultValue: 'ssh:https://github.com/n96perera/jenkins-example.git', description: 'gitLocation field (add git ssh location).')
        
    }
	
    stages { 
	    stage('git clone'){
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
