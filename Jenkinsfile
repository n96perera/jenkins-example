
pipeline {
 agent any
    environment {
        env.JAVA_HOME="${tool 'java 8'}"
        env.PATH="${env.JAVA_HOME}/bin:${env.PATH}"
    }
    stages {
        stage ('Compile Stage') {
            steps {
                withMaven(maven : 'maven_3_5_0') {
                    bat 'mvn clean compile'
                }
            }
        }

        stage ('Testing Stage') {

            steps {
                withMaven(maven : 'maven_3_5_0') {
                    bat 'mvn test'
                }
            }
        }


        stage ('Deployment Stage') {
            steps {
                withMaven(maven : 'maven_3_5_0') {
                    bat 'mvn deploy'
                }
            }
        }
    }
}
