pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('kipnisad')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t kipnisad/api-myip:1.0 .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}


		stage('Push') {

			steps {
				sh 'docker push kipnisad/api-myip:1.0'
			}
		}


		stage('Deploy to K8s')
		{
			steps{
				sshagent(['k8s-jenkins'])
				{
					sh 'scp -r -o StrictHostKeyChecking=no ./k8s-deploy kipnisad@api-host:/k8s-deploy'
					
					script{
						try{
							sh 'ssh kipnisad@api-host kubectl apply -f /path/k8s-deploy --kubeconfig=/path/kube.yaml'

							}catch(error)
							{

							}
					}
				}
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}