FROM mongo:5.0.3

#Σε περίπτωση που θέλουμε να κάνουμε restore backup της mongoBD και έχουμε βάλει το backup στο φάκελο database
#COPY database ./dump #κάνουμε uncomment αυτή την γραμμή


#επίσης κάνουμε uncomment τις παρακάτω γραμμές

#CMD mongod --fork --logpath /var/log/mongodb.log; \
# mongorestore -d database ./dump/; \
# mongod --shutdown; \
# docker-entrypoint.sh mongod

# αν θέλουμε να κάνουμε restore κάνουμε comment την παρακάτω γραμμή
CMD docker-entrypoint.sh mongod
