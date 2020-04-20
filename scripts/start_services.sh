### This script is triggered from within docker contrainer
### to start multiple processes in the same container.
### This script is defined in the CMD option in Dockerfile

# Start actions server in background
rasa run actions --actions actions -v&

# Start rasa server with nlu model
# rasa run --model /app/models --enable-api --log-file rasaibotout.log --endpoints /app/config/endpoints.yml --credentials /app/config/credentials.yml --cors '*' -p 5005
rasa run -u current/ --enable-api --log-file rasaibotout.log --endpoints endpoints.yml --credentials credentials.yml --cors '*' -p $PORT
