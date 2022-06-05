#start docker 
docker-compose -f docker-compose.yml up -d --build
#down docker
docker-compose -f docker-compose.yml down
#see docker 
docker-compose -f docker-compose.yml ps -a
