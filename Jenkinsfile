node {
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        checkout scm
    }

    stage('Build image regexparser') {
        /* This builds the actual image */

        app = docker.build("regexparser")
    }

    // stage('Test image') {
        
    //     app.inside {
    //         echo "Tests passed"
    //     }
    // }

    stage('Push image to ttv registry') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
        docker.withRegistry('https://registry.marketfiler.com', 'ttv_registry') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
                echo "Trying to Push Docker"
    }
    stage('send  and exécute docker compose to swarm') {
    sshPublisher(
publishers: 
[sshPublisherDesc(
    configName: 'v1_mtm_manager_1',
     transfers: [sshTransfer(
         cleanRemote: false, 
         excludes: '', 
execCommand: "sudo docker stack deploy --compose-file /home/mtmuser/projects/regexparser/docker-compose.yml ttv",
//    execCommand:"echo test",
  execTimeout: 120000, 
      flatten: false, 
      makeEmptyDirs: true, 
      noDefaultExcludes: false, 
      patternSeparator: '[, ]+', 
      remoteDirectory: '/projects/regexparser', 
      remoteDirectorySDF: false, 
      removePrefix: '', 
      sourceFiles: '**/docker-compose.yml')], 
      usePromotionTimestamp: false, 
      useWorkspaceInPromotion: false, 
      verbose: true)])
    }
}
