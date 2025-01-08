db.createUser({
    user: process.env.MONGO_ROOT_USERNAME,
    pwd: process.env.MONGO_ROOT_PASSWORD,
    roles: [{ role: "readWrite", db: "taskdb" }]
  });
  
  db = db.getSiblingDB('taskdb');
  
  db.createCollection('tasks');
  
  db.tasks.insertMany([
    {
      title: "Example Task 1",
      description: "This is an example task",
      status: "pending",
      createdAt: new Date()
    },
    {
      title: "Example Task 2",
      description: "This is another example task",
      status: "completed",
      createdAt: new Date()
    }
  ]);
  