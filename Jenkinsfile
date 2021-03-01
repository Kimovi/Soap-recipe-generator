pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh '''
                    cd service2
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service3
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service4
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    '''
                }
            }
        stage('Build'){
            steps{
                sh ''' 
                sudo chmod 666 /var/run/docker.sock
                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u kimovi -p password1234
                sudo docker-compose push
                '''
            }
        }
        stage('Deploy'){
            steps{
                sh '''
                    pwd
                    ls -la

                    '''
            }
        }              
    }
}
