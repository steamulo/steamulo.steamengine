properties ([pipelineTriggers([cron('H 1 * * *')]), disableConcurrentBuilds(), buildDiscarder(logRotator(artifactDaysToKeepStr: '5', artifactNumToKeepStr: '10', daysToKeepStr: '10', numToKeepStr: '5'))])

node ('docker') {
    try {
        stage ('Testing') {
            withPythonEnv('/usr/bin/python3') {
                sh "python -m pip install --upgrade pip"
                // We use another dir, outside the python env
                // so that molecule doesn't lint python lib
                sh "mkdir steamulo.steamengine"
                dir('steamulo.steamengine') {
                    checkout scm
                    sh "python -m pip install -r requirements.txt"
                    ansiColor('xterm') {
                        sh "molecule test --all"
                    }
                }
            }
        }
    } finally {
        cleanWs()
    }
}
