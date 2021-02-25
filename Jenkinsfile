properties ([disableConcurrentBuilds(), buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '10', daysToKeepStr: '10', numToKeepStr: '5'))])

node ('docker') {
    try {
        stage ('Testing') {
            withPythonEnv('/usr/bin/python2.7') {
                // We use another dir, outside the python env
                // so that molecule doesn't lint python lib
                sh "mkdir src"
                dir('src') {
                    checkout scm
                    sh "pip install -r requirements.txt"
                    sshagent (credentials: ['gitlab-key']) {
                        sh "molecule test --all"
                    }
                }
            }
        }
    } finally {
        cleanWs()
    }
}
