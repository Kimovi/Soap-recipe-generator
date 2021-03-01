pipeline{
        agent any
        stages{
            stage('Testing'){
                steps{
                    sh '''
                    cd service-1
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service2
                    pip3 install -r requirements.txt
                    python3 -m pytest --cov=application
                    cd ..
                    cd service-3
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
            
        }
}