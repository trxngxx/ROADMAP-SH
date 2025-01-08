import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';
import {
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
  CircularProgress,
  Paper
} from '@material-ui/core';
import { Delete } from '@material-ui/icons';

const fetchTasks = async () => {
  const { data } = await axios.get(`${process.env.REACT_APP_API_URL}/tasks`);
  return data;
};

function TaskList() {
  const { data: tasks, isLoading, error } = useQuery('tasks', fetchTasks);

  if (isLoading) return <CircularProgress />;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <Paper>
      <List>
        {tasks.map((task) => (
          <ListItem key={task._id}>
            <ListItemText
              primary={task.title}
              secondary={task.description}
            />
            <ListItemSecondaryAction>
              <IconButton edge="end" aria-label="delete">
                <Delete />
              </IconButton>
            </ListItemSecondaryAction>
          </ListItem>
        ))}
      </List>
    </Paper>
  );
}

export default TaskList;
