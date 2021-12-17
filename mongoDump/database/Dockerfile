FROM mongo:5.0.3

# COPY database ./dump

CMD docker-entrypoint.sh mongod

# CMD mongod --fork --logpath /var/log/mongodb.log; \
#     mongorestore -d database ./dump/; \
#     mongod --shutdown; \
#     docker-entrypoint.sh mongod