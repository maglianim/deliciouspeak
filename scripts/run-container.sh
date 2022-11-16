docker run -p 5000:5000 -d deliciouspeak


-- run interattivo con std out e rimosso alla chiusura
docker container run -p 5000:5000 -it --rm deliciouspeak

-- run interattivo con std out e rimosso alla chiusura e bind volume
docker container run -v ~/data:/app/api/db -p 5000:5000 -it --rm deliciouspeak


docker run --name=nginx -d -v ~/nginxlogs:/var/log/nginx -p 5000:80 nginx